def params_filter(sql, max_length=20):
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%", "$",
                   "(", ")", "%", "@", "!", "or", "1=1", "1 = 1"]
    for stuff in dirty_stuff:
        sql = sql.replace(stuff, "")
    return sql[:max_length]