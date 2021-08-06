total_pages = int(input())
page_no = int(input())


def minimum_turns():
    return min(page_no // 2, total_pages // 2 - page_no // 2)


print(minimum_turns())
