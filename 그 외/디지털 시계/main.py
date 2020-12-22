def is_num_include_three(n):
    if str(n).find('3') != -1:
        return True

    return False


hour = 0
minute = 0
second = 0

SECONDS_OF_DAY = 24 * 60 * 60

result = 0

h_three_count = 0
for h in range(24):
    if is_num_include_three(h):
        h_three_count += 1

m_and_s_three_count = 0
for m in range(60):
    if is_num_include_three(m):
        m_and_s_three_count += 1


result += h_three_count * 60 * 60

m_three_count = m_and_s_three_count * (24 - h_three_count)
result += m_three_count * 60

result += (60 - m_and_s_three_count) * m_and_s_three_count * (24 - h_three_count)

print(result)
