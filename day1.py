import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 模擬一組學生的讀書時數和考試分數
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
scores = np.array([40, 50, 55, 60, 65, 70, 75, 85, 88, 95])

# 畫散點圖
plt.scatter(hours, scores, color='blue', label='學生資料')
plt.xlabel('讀書時數')
plt.ylabel('考試分數')
plt.title('讀書時數 vs 考試分數')
plt.legend()
plt.show()

# 基本統計
print("平均讀書時數：", np.mean(hours))
print("平均考試分數：", np.mean(scores))
print("分數標準差：", np.std(scores))