def answer_handler(data):

    # data는 바이트입니다 반드시 decode를 통해 string으로 변환하세요.
    data = data.decode()
    print("data: {}".format(data))
    answer = data

    if 'hello' in data:
        answer = 'Nice to Meet You!'
        return answer
    elif 'bye' in data:
        answer = 'Good Bye'
        return answer
    else:
        return answer