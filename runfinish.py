# -----------------------------------------------------------------------------
# @author dinyusheng
# This is template code of markdown generating by ply
# @update 2014-12-16
# @lience MIT
# -----------------------------------------------------------------------------
import sys

tokens = (
    'Text','Gump','Link','Hn','Cr','Strong','CodeLine','Blockquote','Href','EmWord','LinkWordName','Hr','CodeBlock',
    'Li0','Li1','Li2','Li0spe','Li1spe','Li2spe','Color'
    )

# Tokens
def t_Color(t):
    r'@C\#([0-9A-Fa-f]){6,6}\([^\)]+\)'
    t.value="<span style=\"color:"+str(t.value)[2:9]+"\">"+str(t.value)[10:-1]+"</span>"
    return t
    
def t_Hr(t):
    r'((\*\ *)|(\-\ *)|(=\ *)){3,}|(\*\ \*\ \*)'
    t.value='<HR>'
    return t

t_Blockquote = r'>'

def t_Li2spe(t):
    r'(\t\t(\d)+\.\s)'
    return t

def t_Li1spe(t):
    r'(\t(\d)+\.\s)'
    return t

def t_Li0spe(t):
    r'((\d)+\.\s)'
    return t


def t_Li2(t):
    r'(\t\t(\+|\*)\s)'
    t.value=str(t.value)[2]
    return t

def t_Li1(t):
    r'(\t(\+|\*)\s)'
    t.value=str(t.value)[1]
    return t

def t_Li0(t):
    r'((\+|\*)\s)'
    t.value=str(t.value)[0]
    t.value=t.value[0]
    return t


    
def t_Href(t):
    r'<[^>]+>'
    t.value=str(t.value)
    t.value=t.value[1:-1]
    t.value='<a href="' + t.value+'">' + t.value+ '</a>'
    return t

def t_CodeBlock(t):
    r'```'
    t.value='<pre><code>'
    return t

def t_LinkWordName(t):
    r'\[[^\]]+\]'
    t.value=str(t.value)
    t.value=t.value[1:-1]
    return t

def t_EmWord(t):
    r'(_[^_]+_)|(\*[^(\*)]+\*)'
    t.value=str(t.value)
    t.value=t.value[1:-1]
    t.value='<em>' + t.value+'</em>'
    return t

def t_Strong(t):
    r'(\*\*[^(\*\*)]+\*\*)|(__[^__]+__)'
    t.value=str(t.value)
    t.value='<strong>'+t.value[2:-2]+'</strong>'          ##########
    return t

def t_CodeLine(t):
    r'`[^`]+`'
    t.value=str(t.value)
    t.value='<code>'+t.value[1:-1]+'</code>'
    return t


def t_Gump(t):
    r'!\[gump\]'
    t.value='gump'
    return t

def t_Hn(t):
    r'\#+\ ?'
    t.value=len(str(t.value))
    return t

def t_Cr(t):
    r'(\n\t)?\n+'
    t.lexer.lineno += t.value.count("\n")
#    print t.lexer.lineno
    return t



def t_Link(t):
    r'\([^\)]*\)'
    t.value=str(t.value)
    t.value=(t.value).replace('(','')
    t.value=(t.value).replace(')','')
    return t


def t_Text(t):
    r'[a-zA-Z0-9,\.:\' ]+'
    t.value=str(t.value)
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex
lex.lex()

precedence = ()
names = {}

def p_body_block(p):
    '''body : block'''
    p[0]= '<html lang="en"><head><meta charset="UTF-8"><title></title><style id="system" type="text/css">h1,h2,h3,h4,h5,h6,p,blockquote {    margin: 0;    padding: 0;}body {    font-family: "Helvetica Neue", Helvetica, "Hiragino Sans GB", Arial, sans-serif;    font-size: 13px;    line-height: 18px;    color: #737373;    margin: 10px 13px 10px 13px;}a {    color: #0069d6;}a:hover {    color: #0050a3;    text-decoration: none;}a img {    border: none;}p {    margin-bottom: 9px;}h1,h2,h3,h4,h5,h6 {    color: #404040;    line-height: 36px;}h1 {    margin-bottom: 18px;    font-size: 30px;}h2 {    font-size: 24px;}h3 {    font-size: 18px;}h4 {    font-size: 16px;}h5 {    font-size: 14px;}h6 {    font-size: 13px;}hr {    margin: 0 0 19px;    border: 0;    border-bottom: 1px solid #ccc;}blockquote {    padding: 13px 13px 21px 15px;    margin-bottom: 18px;    font-family:georgia,serif;    font-style: italic;}blockquote:before {    content:"C";    font-size:40px;    margin-left:-10px;    font-family:georgia,serif;    color:#eee;}blockquote p {    font-size: 14px;    font-weight: 300;    line-height: 18px;    margin-bottom: 0;    font-style: italic;}code, pre {    font-family: Monaco, Andale Mono, Courier New, monospace;}code {    background-color: #fee9cc;    color: rgba(0, 0, 0, 0.75);    padding: 1px 3px;    font-size: 12px;    -webkit-border-radius: 3px;    -moz-border-radius: 3px;    border-radius: 3px;}pre {    display: block;    padding: 14px;    margin: 0 0 18px;    line-height: 16px;    font-size: 11px;    border: 1px solid #d9d9d9;    white-space: pre-wrap;    word-wrap: break-word;}pre code {    background-color: #fff;    color:#737373;    font-size: 11px;    padding: 0;}@media screen and (min-width: 768px) {    body {        width: 748px;        margin:10px auto;    }}</style><style id="custom" type="text/css"></style></head><body>' + p[1] + '</body></html>'
    #p[0]='<body>'+p[1]+'</body>'

def p_block_mline(p):
    '''block : mline'''
    p[0]= p[1]

def p_mline_line(p):
    '''mline : line
             | mline line'''
    if(len(p)==2):
        p[0]= p[1]
    if(len(p)==3):
        p[0]=p[1]+p[2]

def p_line(p):
    '''line : Hline
            | gumpline
            | wordlineEnd
            | blockquoteblock
            | Hr Cr
			| CodeBlockEnd Cr
            | Li0Block'''
    p[0]=p[1]+'\n'

def p_CodeBlockText(p):
    '''CodeBlockText : CodeBlock Cr wordlineinit
                    | CodeBlockText Cr wordlineinit'''
    p[0]=p[1]+"\n"+p[3]
    
def p_CodeBlockEnd(p):
    '''CodeBlockEnd : CodeBlockText Cr CodeBlock'''
    p[0]=p[1]+"\n"+"</pre></code>"
   
def p_exp_gump_link(p):
    '''gumpline : Gump Link Cr'''
    p[0]="<img src=\""+p[2]+"\" alt=\"gump\">" +'\n'

def p_exp_Hn_Text(p):
    '''Hline : Hn wordlineinit Cr'''
    p[0] = '<h'+str(((p[1])))+'>' + p[2] + '</h'+str(((p[1])))+'>' +'\n'

def p_wordlineinit_text(p):
    '''wordlineinit : Text
                | specialtext
                | wordlineinit Text
                | wordlineinit specialtext
                | Href'''
    if(len(p)==2):
        p[0]=p[1]
    if(len(p)==3):
        p[0]=p[1]+p[2]

def p_wordlineEnd(p):
    '''wordlineEnd : wordlineinit Cr'''
    p[0]='<p>'+p[1]+'</p>'

def p_special_text(p):
    '''specialtext : Strong 
                | CodeLine
                | EmWord
                | linkword
                | Color'''
    p[0]=p[1]
    
def p_blockquoteLine(p):
    '''blockquoteline : Blockquote wordlineinit Cr
                    | blockquoteline blockquoteline'''  ###
    if(len(p)==3):
        p[0]=p[1]+p[2]
    if(len(p)==4):
        p[0]=p[2]


def p_blockquoteBlock(p):
    '''blockquoteblock : blockquoteline'''
    p[0]='<blockquote><p>'+p[1]+'</p></blockquote>'

def p_linkword(p):
    '''linkword : LinkWordName Link'''
    p[0]='<a href="'+p[2]+'">'+p[1]+'</a>'

def p_Li0List(p):
    '''Li0List : Li0 wordlineinit Cr
                | Li0List Li0List
                | Li0 wordlineinit Cr Li1Block'''
    if(len(p)==4):
        p[0]='<li>'+p[2]+'</li>\n'
    if(len(p)==3):
        p[0]=p[1]+p[2]
    if(len(p)==5):
        p[0]='<li>'+p[2] +'\n'+p[4]+'</li>'

def p_Li0Block(p):
    '''Li0Block : Li0List'''
    p[0]='<ul>'+p[1]+'</ul>'

def p_Li0speList(p):
    '''Li0speList : Li0spe wordlineinit Cr
                | Li0speList Li0speList
                | Li0spe wordlineinit Cr Li1Block'''
    if(len(p)==4):
        p[0]='<li>'+p[2]+'</li>\n'
    if(len(p)==3):
        p[0]=p[1]+p[2]
    if(len(p)==5):
        p[0]='<li>'+p[2] +'\n'+p[4]+'</li>'

def p_Li0speBlock(p):
    '''Li0Block : Li0speList'''
    p[0]='<ol>'+p[1]+'</ol>'    
    
    
def p_Li1List(p):
    '''Li1List : Li1 wordlineinit Cr
                | Li1List Li1List
                | Li1 wordlineinit Cr Li2Block'''
    if(len(p)==4):
        p[0]='<li>'+p[2]+'</li>\n'
    if(len(p)==3):
        p[0]=p[1]+p[2]
    if(len(p)==5):
        p[0]='<li>'+p[2] +'\n'+p[4]+'</li>'


def p_Li1Block(p):
    '''Li1Block : Li1List'''
    p[0]='<ul>'+p[1]+'</ul>\n'
    


def p_Li1speList(p):
    '''Li1speList : Li1spe wordlineinit Cr
                | Li1speList Li1speList
                | Li1spe wordlineinit Cr Li2Block'''
    if(len(p)==4):
        p[0]='<li>'+p[2]+'</li>\n'
    if(len(p)==3):
        p[0]=p[1]+p[2]
    if(len(p)==5):
        p[0]='<li>'+p[2] +'\n'+p[4]+'</li>'

def p_Li1speBlock(p):
    '''Li1Block : Li1speList'''
    p[0]='<ol>'+p[1]+'</ol>\n'
    
def p_Li2List(p):
    '''Li2List : Li2 wordlineinit Cr
                | Li2List Li2List'''
    if(len(p)==4):
        p[0]='<li>'+p[2]+'</li>\n'
    if(len(p)==3):
        p[0]=p[1]+p[2]

def p_Li2speList(p):
    '''Li2speList : Li2spe wordlineinit Cr
                | Li2speList Li2speList'''
    if(len(p)==4):
        p[0]='<li>'+p[2]+'</li>\n'
    if(len(p)==3):
        p[0]=p[1]+p[2]

def p_Li2speBlock(p):
    '''Li2Block : Li2speList'''
    p[0]='<ol>'+p[1]+'</ol>\n'
    
def p_Li2Block(p):
    '''Li2Block : Li2List'''
    p[0]='<ul>'+p[1]+'</ul>\n'

def p_error(p):
    if p:
        print("error at '%s' line '%d'" % (p.value, p.lineno))
    else:
        print("error at EOF")

import ply.yacc as yacc
yaccer=yacc.yacc(method="SLR")

if __name__ == '__main__':
    filename = 'test03.md'
    
    result = yaccer.parse(open(sys.argv[1]).read(),debug=0)
    print result
    outputfile=open("output00.html",'w')
    outputfile.write(result)
    outputfile.close()
    if(len(sys.argv)==3):
        outputfile=open(sys.argv[2],'w')
        outputfile.write(result)
        outputfile.close()