#!/usr/bin/env python
# coding: utf-8

# In[52]:


import numpy as np
import random
import math

#建立顧客、蒐集點、集貨中心List
cut_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10',       #i
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
cp_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10']        #j
crc_list =['1', '2', '3', '4', '5']                                 #k

#各點座標
cut_x = [15.69,18.67,1.6,9.43,49.08,33.14,28.62,24.86,3.42,33.23,45.32,46.37,24.93,28.07,2.77,28.61,38.8,2.13,25.78,45.69]
cut_y = [3.8,24.28,59.13,2.27,54.43,10.85,50,59.39,35.85,21.9,27.23,6.36,32.6,33.38,0.5,51.99,51.71,41.98,2.81,57.24]
cp_x = [43.97,1.57,41.23,5.04,24.79,16.18,30.16,40.32,6.94,54.71]
cp_y = [49.89,12.65,30.25,58.97,19,20.66,45.3,0.4,33.58,57.06]
crc_x = [8.58,32.36,9.58,47.54,20.14]
crc_y = [30.25,28.59,6.51,19.31,53.21]

#dij cut到cp
i = random.randint(0, 19)
j = random.randint(0, 9)
dis_ij = math.sqrt((cut_x[i] - cp_x[j])**2 + (cut_y[i] - cp_y[j])**2)
#djk cp到crc
k = random.randint(0, 4)
dis_jk = math.sqrt((cp_x[j] - crc_x[k])**2 + (cp_y[j] - crc_y[k])**2)

#jk距離懲罰變數beta
if dis_jk < 25:
    beta = 1
elif 25 < dis_jk <= 60:
    beta = 1.1
else:
    beta = 1.2
    
#jk運輸量獎勵變數alpha
if X6 < 200:
    alpha = 1
elif 200 < X6 <= 400:
    alpha = 0.8
else:
    alpha = 0.6

fEab = 1*alpha*beta

#x1 #Zj (01) 蒐集點是否被建置在j
#x2 #ri  i顧客的每日退貨量
#x3 #Yij (01) 消費者i在蒐集點j被收貨
#x4 #Tj  (0~7) 初始點j蒐集期長度
#x5 #Gk  (01) 集貨中心是否被建置在k
#x6 #Xjk 總收貨量

#Zj 定義為隨機產生01
x1 = {'1':random.randint(0,1),'2':random.randint(0,1),'3':random.randint(0,1),
      '4':random.randint(0,1),'5':random.randint(0,1), '6': random.randint(0,1),
      '7':random.randint(0,1),'8':random.randint(0,1), '9':random.randint(0,1),'10':random.randint(0,1)}

#ri顧客每日退貨量
x2 = {'1':12,'2':43,'3':34,'4':21,'5':19,
      '6':10,'7':37,'8':22,'9':35,'10':29,
      '11':22,'12':21,'13':11,'14':327,'15':44,
      '16':41,'17':46,'18':22,'19':37,'20':45}
#Yij
x3 = {'1': random.randint(0,1),'2':random.randint(0,1),'3':random.randint(0,1),
      '4':random.randint(0,1),'5':random.randint(0,1), '6': random.randint(0,1),
      '7':random.randint(0,1),'8':random.randint(0,1), '9':random.randint(0,1),'10':random.randint(0,1),
     '11': random.randint(0,1),'12':random.randint(0,1),'13':random.randint(0,1),
      '14':random.randint(0,1),'15':random.randint(0,1), '16': random.randint(0,1),
      '17':random.randint(0,1),'18':random.randint(0,1), '19':random.randint(0,1),'20':random.randint(0,1)}

#Tj 定義為隨機產生0~7
x4 = {'1': random.randint(0,7),'2':random.randint(0,7),'3':random.randint(0,7),
      '4':random.randint(0,7),'5':random.randint(0,7), '6': random.randint(0,7),
      '7':random.randint(0,),'8':random.randint(0,7), '9':random.randint(0,7),'10':random.randint(0,7)}

#Gk 定義為隨機產生01
x5 = {'1': random.randint(0,1),'2':random.randint(0,1),'3':random.randint(0,1),
      '4':random.randint(0,1),'5':random.randint(0,1)}


#最小成本目標函數
#obj1= a*np.sum(x1[j] for j in cp_list)+b*w*np.sum(np.sum(x2[j]*x3[i][j]*(x4+1)/2 for j in cp_list) for i in cut_list)
#obj2 =  np.sum(qk*x5[k] for k in crc_list) + np.sum ((x5*np.sum(x6[j][k]*w/x[3] for j in cp_list) * (E*alpha*beta)) for k in crc_list)
#minZ = obj1 + obj2 + h*w*np.sum(x2[i] for i in cut_list)

#直接定義決策變數
200*x1 + 0.1*250*(x2*x3*((x4+1)/2) + 0.1*250*x2 + 3000*x5 + x5*x6*250/x4 * fEab

#設定限制式
np.sum(x3[j] for j in cp_list) = 1
np.sum(x3[i] for i in cut_list) <= 9999999}, #大M值限制
np.sum(x2[i]*x3[i]*x4[i] for i in cut_list) = np.sum(x6[k] for k in crc_list)
np.sum(x6[j]for j in cp_list) <= mk*x5
dis_ij * x3 <= 25 
np.sum(x1[j] for j in cp_list) >= 1
np.sum(x5[k] for k in crc_list) >= 1

#自訂初始解[Zj, ri, Yij, Tj, Gk, Xjk]
[x1, x2, x3, x4, x5, x6] = [5, 420, 10, 3, 3, 28]


# In[34]:


import matplotlib.pyplot as plt
cut_x = [15.69,18.67,1.6,9.43,49.08,33.14,28.62,24.86,3.42,33.23,45.32,46.37,24.93,28.07,2.77,28.61,38.8,2.13,25.78,45.69]
cut_y = [3.8,24.28,59.13,2.27,54.43,10.85,50,59.39,35.85,21.9,27.23,6.36,32.6,33.38,0.5,51.99,51.71,41.98,2.81,57.24]
cp_x = [43.97,1.57,41.23,5.04,24.79,16.18,30.16,40.32,6.94,54.71]
cp_y = [49.89,12.65,30.25,58.97,19,20.66,45.3,0.4,33.58,57.06]
crc_x = [8.58,32.36,9.58,47.54,20.14]
crc_y = [30.25,28.59,6.51,19.31,53.21]
plt.scatter(cut_x, cut_y, color='b', label = 'cut')
plt.scatter(cp_x, cp_y, color='r', marker = 's', label ='cp' )
plt.scatter(crc_x, crc_y, color='m',marker = '^', label = 'crc')
plt.legend()
plt.show()


# 給助教&老師：不好意思進度沒有抓好，deadline前仍沒有完整的結果。
# 還沒放棄!! 我們會繼續嘗試，並補上檔案以供未來學弟妹參考。 不好意思，謝謝!
# by 聞祈&依蓉 1/14
