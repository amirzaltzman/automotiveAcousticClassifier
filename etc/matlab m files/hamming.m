function c = hamming(m)

if (m == 1)
    c = 1;
else
    m = m - 1;
    c = 0.54 - 0.46 * cos (2 * pi * (0:m)' / m);
end




