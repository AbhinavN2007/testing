def arithmetic_arranger(problems,show_answer=False):
    final_list=[]
    
    
    if len(problems)>5:
        return("Only 5 problems at a time")
    else:
        for problem in problems:

            if " + " in problem:
                problem_current=problem.split(" + ")
                if not problem_current[0].isdigit() or not problem_current[1].isdigit():
                    return("Error not a number")
                else:
                    if len(problem_current[0])>4 or len(problem_current[1])>4:
                        return("too long numbers")
                    else:
                        a=problem_current[0]
                        b=problem_current[1]
                        row1_length=len(a)
                        row2_length=len(b)
                        row3_length=len(str(int(a)+int(b)))
                        
                        row1_list=list(a)
                        row2_list=list(b)
                        row3_list=list(str(int(a)+int(b)))
                        
                        while len(row1_list)<max(row1_length,row2_length,row3_length):
                            row1_list.insert(0,' ')
                        
                        while len(row2_list)<max(row1_length,row2_length,row3_length):
                            row2_list.insert(0,' ')
                        
                        while len(row3_list)<max(row1_length,row2_length,row3_length):
                            row3_list.insert(0,' ')
                        if show_answer:

                            final_string='  '+''.join(row1_list)+'\n'+'+ '+''.join(row2_list)+'\n'+'--'+'-'*max(len(row1_list),len(row2_list),len(row3_list))+'\n'+'  '+''.join(row3_list)
                        else:
                            final_string='  '+''.join(row1_list)+'\n'+'+ '+''.join(row2_list)+'\n'+'--'+'-'*max(len(row1_list),len(row2_list),len(row3_list))
                        final_list.append(final_string)
            else:
                problem_current=problem.split(" - ")
                if not problem_current[0].isdigit() or not problem_current[1].isdigit():
                    return("Error not a number")
                else:
                    if len(problem_current[0])>4 or len(problem_current[1])>4:
                        return("too long numbers")
                    else:
                        a=problem_current[0]
                        b=problem_current[1]
                        row1_length=len(a)
                        row2_length=len(b)
                        row3_length=len(str(int(a)-int(b)))
                        
                        row1_list=list(a)
                        row2_list=list(b)
                        row3_list=list(str(int(a)-int(b)))
                        
                        while len(row1_list)<max(row1_length,row2_length,row3_length):
                            row1_list.insert(0,' ')
                        
                        while len(row2_list)<max(row1_length,row2_length,row3_length):
                            row2_list.insert(0,' ')
                        
                        while len(row3_list)<max(row1_length,row2_length,row3_length):
                            row3_list.insert(0,' ')
                        if show_answer:

                            final_string='  '+''.join(row1_list)+'\n'+'- '+''.join(row2_list)+'\n'+'--'+'-'*max(len(row1_list),len(row2_list),len(row3_list))+'\n'+'  '+''.join(row3_list)
                        else:
                            final_string='  '+''.join(row1_list)+'\n'+'- '+''.join(row2_list)+'\n'+'--'+'-'*max(len(row1_list),len(row2_list),len(row3_list))
                        final_list.append(final_string)
            

    columns = [s.splitlines() for s in final_list]
    widths = [max(len(line) for line in col) for col in columns]

    # Pad lines in each column to its corresponding width
    padded_columns = [
        [line.ljust(widths[i]) for line in col]
        for i, col in enumerate(columns)
    ]

    # Zip corresponding lines horizontally and join per row
    rows = ["  ".join(row) for row in zip(*padded_columns)]

    # Join rows into a single string for display
    final_str = "\n".join(rows)

    return(final_str)
print(arithmetic_arranger(['25 + 36','35 - 450','0 - 10'],show_answer=True))

                            
                            
                                

                                