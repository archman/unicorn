# -*- coding: utf-8 -*-

from fn_utils import flip_data_str_signs


# C4
C4_xdata = "0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6"
C4_ydata = "2.17E-04 4.34E-04 6.51E-04 8.69E-04 1.09E-03 1.31E-03 1.52E-03 1.74E-03 1.96E-03 2.18E-03 2.40E-03 2.61E-03"

# C4S4
C4S4_xdata = C4_xdata
C4S4_ydata = "1.61E-04 3.23E-04 4.86E-04 6.48E-04 8.10E-04 9.73E-04 1.14E-03 1.30E-03 1.46E-03 1.62E-03 1.79E-03 1.95E-03"

# C9Q10
C9Q10_xdata = "5 10 15 20 25 30 35 40 45"
C9Q10_ydata = "9.10E-04 1.85E-03 2.80E-03 3.77E-03 4.75E-03 5.73E-03 6.71E-03 7.69E-03 8.67E-03"

# C_S1 !!!need data!!! use C9Q10 temporarily
C_S1_xdata = "5 10 15 20 25 30 35 40 45"
C_S1_ydata = "9.10E-04 1.85E-03 2.80E-03 3.77E-03 4.75E-03 5.73E-03 6.71E-03 7.69E-03 8.67E-03"

# S4
S4_xdata = "20 40 60 80 100 120 140 160 180 200 220 240 260 280 300"
S4_ydata = "-0.0580025822 -0.1161043395 -0.1742150116 -0.2323199102 -0.2904142629 -0.3484930598 -0.4065498774 -0.4645751634 -0.5225515915 -0.5804477477 -0.6381945325 -0.695612072 -0.7522088229 -0.8071705002 -0.8600727249"

# S1 !!!need data!!! use S4 temporarily
S1_xdata = "20 40 60 80 100 120 140 160 180 200 220 240 260 280 300"
S1_ydata = "-0.0580025822 -0.1161043395 -0.1742150116 -0.2323199102 -0.2904142629 -0.3484930598 -0.4065498774 -0.4645751634 -0.5225515915 -0.5804477477 -0.6381945325 -0.695612072 -0.7522088229 -0.8071705002 -0.8600727249"

# Q8
Q8_xdata = "5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195"
Q8_ydata = "7.22E-01 1.4620182 2.2147799 2.9789081 3.74636465 4.5141563 5.2823165 6.0503965 6.818065 7.5852735 8.3515665 9.116546 9.879853 10.641093 11.3996425 12.154415 12.90472 13.6492715 14.387268 15.115826 15.8311425 16.5290995 17.206694 17.853351 18.4489535 18.9707085 19.4555835 19.9028745 20.316784 20.699379 21.0560485 21.387474 21.6947125 21.979232 22.243236 22.490041 22.7214665 22.9390785 23.1430245"

# Q9
Q9_xdata = "5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195"
_Q9_ydata = "0.72550564 1.4696342 2.2217468 2.9855075 3.7537958 4.5232289 5.2926941 6.0623996 6.8318876 7.6010907 8.3698891 9.1379508 9.9049769 10.670703 11.434844 12.197023 12.956649 13.712886 14.465165 15.212488 15.954278 16.688388 17.412428 18.12207 18.815421 19.485131 20.125557 20.706961 21.231033 21.718338 22.168227 22.586361 22.98009 23.344792 23.68743 24.006866 24.302281 24.580829 24.840906"
Q9_ydata = flip_data_str_signs(_Q9_ydata) 
