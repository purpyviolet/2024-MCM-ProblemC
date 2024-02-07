# our work

### Problem1

1. 首先第一题我们分了两个方面来解决，首先是Hodrick-Prescott滤波器，趋势分量和周期分量分离分析得到了基本的比赛局势变化

2. 之后通过主观描述性分析以及客观的Topsis分析法量化了“势头”的概念，得到了基本的评价指标

3. 之后分析了整场比赛的势头变化



### Problem 2

1. 首先通过得分差异与势头的Granger因果关系检验势头与选手分差之间的显著关系
2. 之后检验势头差与比赛选手输赢之间的关系，用皮尔逊以及斯皮尔曼相关系数验证势头差对于预测比赛输赢的准确度
3. 最后用cumsum算法分析势头的转折点，并进行游程检验，来分析势头变化与转折点的显著性是否呈现随机性



### Problem 3

1. 定义新参数swing作为比赛流程波动性的指标（原势头、连胜参数以及运动员体力）
2. 数据预处理，将文本格式信息转换为二进制
3. 对比所有预测swing的模型，比较mae与mape寻找最佳预测模型→基于XGBoost的swing预测模型
4. 进行shap分析，得到各特征对于swing参数的影响相关性
5. 基于Swing预测模型和模拟退火的战略推进，分析对于比赛波动改变策略的近优解



### Problem 4

1. 将原本模型运用在wimbledon女子网球联赛、美国网球锦标赛以及男子乒乓球比赛中，验证模型效果以及泛化能力
2. 分析不同比赛中的首要波动影响参数，提出模型优化建议



```mermaid
graph TD
    A[问题1开始] --> B[使用Hodrick-Prescott滤波器分析趋势和周期分量]
    B --> C[通过描述性和TOPSIS分析量化势头]
    C --> D[分析整场比赛的势头变化]
    D --> E[问题1结束]

    F[问题2开始] --> G[势头与分差的Granger因果关系检验]
    G --> H[势头差与比赛输赢的相关性分析]
    H --> I[使用CUMSUM算法和游程检验分析势头转折点]
    I --> J[问题2结束]

    K[问题3开始] --> L[定义新参数swing]
    L --> M[数据预处理转换为二进制]
    M --> N[比较模型找到最佳swing预测模型]
    N --> O[进行SHAP分析]
    O --> P[基于Swing模型和模拟退火的战略推进]
    P --> Q[问题3结束]

    R[问题4开始] --> S[模型应用于不同比赛验证效果]
    S --> T[分析首要波动影响参数提出优化建议]
    T --> U[问题4结束]

```

```mermaid
graph TD
    A[Problem 1 Start] --> B[Use Hodrick-Prescott filter for trend and cycle component analysis]
    B --> C[Quantify momentum concept through descriptive and TOPSIS analysis]
    C --> D[Analyze momentum changes throughout the match]
    D --> E[Problem 1 End]

    F[Problem 2 Start] --> G[Test the significant relationship between momentum and score difference with Granger causality]
    G --> H[Analyze the relationship between momentum difference and match outcome using Pearson and Spearman coefficients]
    H --> I[Analyze momentum turning points with CUMSUM algorithm and run test]
    I --> J[Problem 2 End]

    K[Problem 3 Start] --> L[Define new parameter swing as an indicator of match process volatility using AHP]
    L --> M[Data preprocessing to convert textual information into binary]
    M --> N[Compare all models to find the best for predicting swing using MAE and MAPE → XGBoost-based swing prediction model]
    N --> O[Perform SHAP analysis to understand the impact of features on swing parameter]
    O --> P[Strategic advancement based on Swing prediction model and simulated annealing for near-optimal solution to match fluctuations]
    P --> Q[Problem 3 End]

    R[Problem 4 Start] --> S[Apply the original model in Wimbledon women's tennis, US Open, and men's table tennis matches to verify effectiveness and generalization ability]
    S --> T[Analyze primary fluctuation influencing parameters in different matches and suggest model improvements]
    T --> U[Problem 4 End]

```

