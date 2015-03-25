def add_line_number(in_file, out_file):
    in_f = open(in_file, 'r')
    out_f = open(out_file, 'w')
    lines = in_f.readlines()
    l = 1
    for line in lines:
        # out_f.write('{} {}'.format(l, line))
        # out_f.write(str(l) + ' ' + line)
        out_f.write(' '.join([str(l), line]))
        l += 1
    out_f.close()
    in_f.close()
