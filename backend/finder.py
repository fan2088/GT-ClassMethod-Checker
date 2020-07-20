def find_valid_result(data, className, sectionName):
    if (className == ''):
        return list()
    elif (className != '' and sectionName == ''):
        result = []
        for i in range (0, len(data)):
            if data[i]['Class'] == className:
                result.append(data[i])
            i += 1
        return result
    else:   
        result = []
        for i in range (0, len(data)):
            if data[i]['Class'] == className and data[i]['Section'] == sectionName:
                result.append(data[i])
            i += 1
        return result
