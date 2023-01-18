def por_v_grig(year, day_count):
    is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    d_in_m = [31, 28 + is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(len(d_in_m) ):
        if day_count <= d_in_m[i]:
            return day_count, i + 1
        day_count -= d_in_m[i]

print(por_v_grig(1999, 113))

#Вывод
(23, 4)