#n = 5 
#m = 3
#1,2,3,4,5
# 0 0 0 0
#0 [[1,4,10,20,35],
#0 [0,2,2,    ],
#0 [   ]]
# 1 2 3 4 5
# 1 3 6 10 15
# 5
# 1 3 -->10-3-2=5
# 2 4 -->

#[[2,10,31,69,128]
# [2,8,23,46,82]
# [2,8,21,40,67]
# [2,8,21,38,61]
# [2,8,21,38,59]]

#vahid
#[[0,2,10,31,69,128,211, 320]0
# [0,2,8, [23],46,82,129, 191]1 8=> 10-2/23=>31-8/46=>69-23/82=>128-46 (ok)
# [0,[2,8],21,40,67, 104, 149]2 21=> 23-2+0/40=> 46-8+2/67=>82-21+8-2
# [[0,2],8,21,38,61, 91,130]3 38=> 40-2+0/61=>67-8+2
# [0,2,8,21,38,59, 85, 117]]4 59=> 61-2
#wastingggggg timeeeeeee

#(191, [[0, 2, 15, 36, 62], [0, 6, 23, 47]])
#149 [[0, 2, 19, 45], [0, 6, 27], [0, 13, 37]]
 
# [[0, 2, 10, 31, 69, 128]
# [0, 2, 8, 25, 50, 97],
# [0, 2, 8, 23, 44, 80]]

#[[0, 2, 10, 31, 69, 128]
# , [0, 2, 8, 25, 50, 97], 
# [0, 2, 8, 23, 44, 80],
#  [0, 2, 8, 23, 42, 74],
#  [0, 2, 8, 23, 42, 72]]


#mehrshad joooooonsk
# [0,  2,6,13,17,21]
#[[0,2,10,31,69,128]1 => 
# [0,2,8, 23,46,82]2 => 23=31-10+2-0 / 46=69-31+10-2+0/82=128-69+31-10+2-0
# [0,2,8,21,40,67]3 =>61=67-8+2 / 67 = 82-46 +23 -8 +2 -0 (53)
# [0,2,8,21,38,61]4 => 59 = 61-2+0
# [0,2,8,21,38,59]]5

