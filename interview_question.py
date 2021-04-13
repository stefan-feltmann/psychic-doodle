def solution(input_array):
    output = []
    return recursion(output, input_array)

def recursion(output, input_array):
    for i in input_array:
        if(isinstance(i, list)):
            recursion(output, i)
        else:
            output.append(i)
    return output


if __name__ == "__main__":
    input = [['one','two',['three', ['four', ['five', 'six', ['seven', ['eight']]]]]],'nine']
    print(solution(input))