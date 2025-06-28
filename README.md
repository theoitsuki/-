# 声の主観的評価と音声特徴量の相関分析
本プロジェクトは、音声の主観的な評価（好み，聞き取りやすさなど）が、どのような音声特徴量（基本周波数、各MFCC次元、db）と相関があるのかを分析することを目的としています。この分析により、音声品質の客観的な指標と人間の知覚との関連性を明らかにします。

├── src  
│   ├── get_features.ipynb  
│   ├── mfcc_maxspc.ipynb  
│   └── liner_regression.ipynb  
├── dataProcessor.py  
├── dataset  
│   ├── data.csv  
│   └── predata.xlsx  
└── README.md  

以下ディレクトリ構造

以下ディレクトリ構造
* `src/`: ソースコードを格納します。
    * `src/get_features.ipynb/`: 音声データの読み込み、前処理、特徴量抽出に関するスクリプト。
    * `src/mfcc_maxspc.ipynb/`: 統計的な相関分析を行うスクリプト。
    *  `src/liner_regression.ipynb/`: 統計的な相関分析を行うスクリプト。
    * `src/dataProcesser.py/`: 分析結果を可視化するためのスクリプト。
* `dataset/`: データファイルを格納します。
    * `dataset/data.csv/`: 元の音声ファイルを配置します。
    * `dataset/実験設問回答.xlsx/`: 処理済みデータや抽出された特徴量ファイルを保存します。

