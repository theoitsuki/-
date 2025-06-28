# 声の主観的評価と音声特徴量の相関分析
本プロジェクトは、音声の主観的な評価（好み，聞き取りやすさなど）が、どのような音声特徴量（基本周波数、各MFCC次元、db）と相関があるのかを分析することを目的としています。この分析により、音声品質の客観的な指標と人間の知覚との関連性を明らかにします。

├── src  
│   ├── get_features.ipynb  
│   ├── mfcc_maxspc.ipynb  
│   ├── liner_regression.ipynb  
│   └── dataProcessor.py  
├── 
├── dataset  
│   ├── data.csv  
│   └── predata.xlsx  
└── README.md  

* `src/`: ソースコードを格納します。
    * `src/get_features.ipynb/`: 音声データの読み込み、前処理、特徴量抽出を行い、統計的な相関分析を行うスクリプト。
    * `src/mfcc_maxspc.ipynb/`: MFCCの各次元の特徴を可視化するためのスクリプト。
    *  `src/liner_regression.ipynb/`: 研究発表後、考察の一部を行うスクリプト。
    * `src/dataProcesser.py/`: 特徴量抽出の関数を格納しているスクリプト。
* `dataset/`: データファイルを格納します。
    * `dataset/data.csv/`: 解析を行うためにpredata.xlsxに処理を行ったデータ。
    * `dataset/predata.xlsx/`: 処理する前のgoogleformから取得した、被検者100人分リッカート尺度で得たアンケートデータ。

