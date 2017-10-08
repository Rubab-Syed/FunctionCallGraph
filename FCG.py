# -*- coding: utf-8 -
import sys

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.tree.Trees import Trees
from python2Lexer import python2Lexer
from python2Parser import python2Parser
from python2Listener import python2Listener

class Graph:
    def __init__(self):
        self.nodes = OrderedDict()
        self.edges = OrderedDict()

    def add_edge(self, src, dst):
        if src in self.edges:
            self.edges[src].append(dst)
        else:
            self.edges[src] = [dst]

    def add_node(self, function_name):
        self.nodes[function_name] = True

    def __str__(self):
        return "edges: " + self.edges.__str__() + ", functions:　" + list(self.nodes.keys()).__str__()

    def toDOT(self):
        funcs = ""
        for f in self.nodes.keys():
            funcs += f + ';'
        edges = ""
        for (key, value) in self.edges.items():
            if key == None:
                key = "Module"
            for dst in value:
                edges += "  " + key + " -> " + dst + ";\n"

        tpl_str = """
digraph G {
  ranksep=.25;
  edge [arrowsize=.5]
  node [shape=circle, fontname="ArialNarrow",
        fontsize=10, fixedsize=true, height=1];

  $func_list
$edge_list
}
"""
        tpl = Template(tpl_str)
        return tpl.substitute(func_list=funcs, edge_list=edges)


class FunctionListener(python2Listener):
    def __init__(self):
        self.graph = Graph()
        self.current_function_name = None

    def enterFuncdef(self, ctx = python2Parser.FuncdefContext):
        name = ctx.ID().getText()
        self.current_function_name = name
        self.graph.add_node(name)

    def enterFunccall(self, ctx = python2Parser.FunccallContext):
        name = ctx.ID().getText()
        self.graph.add_node(name)

    def exitFunccall(self, ctx):
        name = ctx.ID().getText()
        self.graph.add_edge(self.current_function_name, name)


if __name__ == '__main__':
    input_stream = FileStream(sys.argv[1])
    lexer = python2Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = python2Parser(token_stream)
    tree = parser.top()

    #lisp_tree = tree.toStringTree(recog=parser)
    #print(lisp_tree)

    walker = ParseTreeWalker()
    collector = FunctionListener()
    walker.walk(collector, tree)
    #print(collector.graph)
    f = open("output.dot","w")
    f.write(collector.graph.toDOT())
    f.close()

