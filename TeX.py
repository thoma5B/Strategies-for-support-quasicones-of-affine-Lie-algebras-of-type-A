
def Output(data_string = ""):
    output_string = "\documentclass[10pt,a4paper]{elsarticle} \n" \
    + "\\usepackage{amsmath} \n" \
    + "\\usepackage{amssymb} \n" \
    + "\\usepackage[hmargin=1.5cm, vmargin=1.5cm]{geometry} \n" \
    + "\\begin{document} \n \\scriptsize" \
    + " all quasi-cones on start w.r.t. "\
    + "$V_{\lambda-\delta}$, whereas $V_{\\lambda}=\\left\\{0\\right\\}$ \n\n" \
    + data_string \
    + "\n \\end{document}"
    return output_string

#    output_string += "\n total number of considered quasicones: "\
#                    + str(cones_counter)


def Matrix_to_Latex_string(Matrix, n = 0):
    #if n == 0: n = len(Matrix)
    local_string = " $\left(\\begin{array}{"
    for i in range (0, n ): 
        local_string += "c"
    local_string += "} \n"
    #print(Matrix)
    for i in range (0, n ):
        for j in range (0, n ):
            local_string += str(Matrix[i, j])
            if not j == n - 1: local_string += " & "
        if not i == n - 1: local_string += "\\\\ \n"
    local_string += "\n \end{array}\\right)$ "
    return local_string


def Transform_to_Latex_string(root):  
    return " $\overset{e_{\\alpha_{" \
                    + str(root[0]) + "} + (" \
                    + str(root[1]) + ")\\cdot\\delta" \
                    + "}}{\\rightsquigarrow}$ "


def Strategy_to_TeX(in_list_of_Quasicones):
    data_string = ""
    for C in in_list_of_Quasicones:
        data_string += str(C.enumerator)
        n = len(C._C) 
        data_string += Matrix_to_Latex_string(C._C, n)
        while C.Operator_sequence:
            #print(C.Operator_sequence.pop(0))
            data_string += Transform_to_Latex_string(C.Operator_sequence.pop(0))
            data_string += Matrix_to_Latex_string(C.Transform_sequence.pop(0), n)
        data_string += "\n\n \\hfill w.r.t. $ V_{\\lambda +("\
                                + str(C.delta) + ")\\cdot\\delta } $ \n"
        data_string += "\\begin{align*} \\Rightarrow \#C - \#C' =  "\
                                + str(C.balance)\
                                + " \\end{align*}  \n\n"
    return data_string


def Quasicones_to_TeX(list_of_Quasicones):
    data_string = ""
    for C in list_of_Quasicones:
        n = len(C) 
        data_string += Matrix_to_Latex_string(C, n)
    return data_string
