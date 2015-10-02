

def Output_as_Graph(data_string = ""):
    output_string = "\documentclass{minimal}[12pt] \n \
\\usepackage{amsmath} \n \
\\usepackage{amssymb} \n \
\\usepackage{tikz} \n \
\\usepackage{tkz-berge} \n \
\\usepackage{fp} \n \
\\usepackage[paperwidth=25cm, paperheight=820cm,margin=2pt]{geometry} \n \
\\begin{document} \n \
\\begin{tikzpicture} " \
    + data_string \
    + "\end{tikzpicture} \
\n \\end{document}"
    return output_string

        

def Tree_to_TeX(Tree):
    
    def y_coord(tree_index):
        y = 1
        maxslope = 6
        for i, number in enumerate(tree_index):
            y += maxslope*(number - max_no_of_strategies/2)*20**(-i)
        return y
    
    def node(tree_index):
        data_string = ""
        for i in tree_index:
            data_string += str(i) + "_"
        return data_string

    data_string = ""
    max_no_of_strategies = float(17)
    stretch_x = 3
    stretch_y = 1.2
    total_index_list = []
    for C, index_list in Tree.iteritems():
        #print "index_list ", index_list
        color = index_list.pop(0)
        for tree_index in index_list:
            total_index_list.append(tree_index)
            #print tree_index
            nod = node(tree_index)
            x = 1 + (len(tree_index)-1)*stretch_x
            y = y_coord(tree_index)*stretch_y
            if color:
                data_string += \
    "\\node[circle,draw,fill=red,inner sep=1pt] ("+nod+") at ("+str(x)+","+str(y)+"){}; \n"
            else:
                data_string += \
    "\\node[circle,draw,fill=gray,inner sep=1pt] ("+nod+") at ("+str(x)+","+str(y)+"){}; \n"
    
    total_index_list.sort(key=len)
    while total_index_list:
        dest = total_index_list.pop()
        orig = dest[:-1] 
        #if orig: print total_index_list.index(orig)
        if not orig or orig not in total_index_list: continue        
#        if type(Tree[C][0]) == int:
#            data_string += "\draw[red] ("+str(orig)+") -- ("+str(dest)+");"
#        else:
        data_string += "\\draw[thin] ("+node(orig)+") -- ("+node(dest)+"); \n"
    
    return data_string
    
