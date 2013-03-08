# -*- coding: utf-8 -*-
from lxml.etree import parse
import subprocess
import json

def loadOrdownload(url, filename):
    """Tenta abrir o arquivo (filename) se não conseguir, baixa da (url) com wget."""
    try:
        arquivo = open("../data/" + filename, "r")
        print filename + " file found... loading..."
        return arquivo
    except:
        print filename + " file not found... getting online..."
        subprocess.call(["wget",url,"-O","data/"+filename])
        arquivo = open("../data/"+filename, "r")
        return arquivo
    
def carregaDeputados():
    """Carrega o arquivo XML com os deputados em exercício e extrai os campos necessários"""
    deputados = loadOrdownload("http://www.camara.gov.br/SitCamaraWS/Deputados.asmx/ObterDeputados","deputados.xml")
    soup = parse(deputados)
    lista_deputados = {}
    for d in soup.xpath("//deputado"):
        deputado = {
            "nome" : "",
            "comissoes" : [],
            "proposicoes" : []
        }
        deputado["nome"] = d.xpath("./nomeParlamentar")[0].text
        deputado["partido"] = d.xpath("./partido")[0].text
        deputado["estado"] = d.xpath("./uf")[0].text
        deputado["id"] = d.xpath("./ideCadastro")[0].text
        for comissao in d.xpath(".//comissao"):
            deputado["comissoes"].append(comissao.get("sigla"))
        lista_deputados[deputado["id"]] = deputado
    return lista_deputados

def carregaProposicoes(ano, tipo, lista_deputados):
    """Carrega o arquivo XML com as proposições de um determinado tipo e ano e monta uma lista por deputado"""
    proposicoes = loadOrdownload("http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx/ListarProposicoes?sigla="+tipo+"&numero=&ano="+ano+"&datApresentacaoIni=&datApresentacaoFim=&autor=&parteNomeAutor=&siglaPartidoAutor=&siglaUFAutor=&generoAutor=&codEstado=&codOrgaoEstado=&emTramitacao=", tipo+"_"+ano+".xml")
    soup = parse(proposicoes)

    for p in soup.xpath("//proposicao"):
        proposicao = {}
        proposicao["id"] = p.xpath("./id")[0].text
        proposicao["nome"] = p.xpath("./nome")[0].text
        proposicao["ementa"] = p.xpath("./txtEmenta")[0].text
        deputado_id = p.xpath("./autor1/idecadastro")[0].text.strip()
        try:
            lista_deputados[deputado_id]["proposicoes"].append(proposicao)
        except:
            print "Error on "
            print proposicao
    return lista_deputados

def preparaLista():
    """Prepara a lista de deputados e proposições"""
    tipos = ["PL","PEC"]
    anos = ["2011", "2012"]
        

    lista_deputados = carregaDeputados()    
    for tipo in tipos:
        for ano in anos:
            lista_deputados = carregaProposicoes(ano, tipo,lista_deputados)
    return lista_deputados
    

def listaComissoes(lista_deputados):
    """Cria uma lista com todas as comissoes"""
    comissoes = []
    for deputado in lista_deputados:
        comissoes = comissoes + lista_deputados[deputado]["comissoes"]
    comissoes = list(set(comissoes))
    return comissoes

def escreveDados():
    """Escreve os arquivos JSON das comissões na pasta publica"""
    lista_deputados = preparaLista()
    comissoes = listaComissoes(lista_deputados)
    for comissao in comissoes:
        lista_simples = []
        for deputado in lista_deputados:
            if comissao in lista_deputados[deputado]["comissoes"]:
                lista_simples.append(lista_deputados[deputado])

        comissao = open("../public/data/"+comissao+".json", "w")
        comissao.write(json.dumps(lista_simples, sort_keys=True, indent=4, separators=(',', ': ')));
        comissao.close()


escreveDados()
