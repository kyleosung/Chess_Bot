from __future__ import annotations
import chess
from chess.engine import PlayResult, Limit
from chess import Move
import random
from lib.engine_wrapper import MinimalEngine, MOVE
from typing import Any
import logging


# Use this logger variable to print messages to the console or log files.
# logger.info("message") will always print "message" to the console or log file.
# logger.debug("message") will only print "message" if verbose logging is enabled.
logger = logging.getLogger(__name__)

import sys
sys.path.insert(1, '..')

import chess_DL1_lib as lib
import torch



import joblib

# from sklearn.neighbors import KNeighborsRegressor


'''--------------------------------------------------
LOAD TORCH MODELS'''

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# model9_loaded = torch.load('../models_EL/model_E9-1.pth', map_location=device)


model_loaded = torch.load('../models_EL/model_DL1-3.pth', map_location=device)

'''--------------------------------------------------
LOAD SK MODELS'''

# models_to_load = ['RF_1', 'SVR_1', 'LR_1']
# sk_models_list = []

# for i, model_name in enumerate(models_to_load):
#     sk_models_list.append(joblib.load(f'../models_SK/model_{model_name}.joblib'))


# X_train, X_test, y_train, y_test = SKlib.load_data_XY_a_to_d()
# knn2 = KNeighborsRegressor(n_neighbors=2)
# knn2.fit(X_train, y_train)
# models_list.append(knn2)





counter = 1





class ExampleEngine(MinimalEngine):
    """An example engine that all homemade engines inherit."""

    def search(self, board: chess.Board, *args: Any, **xargs: Any) -> PlayResult:

        global model_loaded
        global sk_models_list
        global counter
        counter += 1

        print(f'Predicting for move {counter}')
        # prediction = lib7.predict(model_loaded, board.fen(), move_number=counter)

        # prediction = lib8.predict78(model7_loaded, model8_loaded, board.fen(), move_number=counter, stochastic=True)
        # prediction = lib8.predict(model_loaded, board.fen(), move_number=counter)
        # prediction = libEns.predict_ensemble(model_loaded, board.fen(), sk_models_list, weights=[0.5, 0.25, 0.25], dl_to_sk=0.9, move_number=0, stochastic=True)

        prediction = lib.predict(model_loaded, board.fen(), move_number=counter, stochastic=True)
        

        
        # Uncomment this line for ensemble prediction
        # prediction = libEns.predict_ensemble(model_loaded, board.fen(), models_list, move_number = counter, dl_to_sk=0.9)



        # move = Move.from_uci(prediction)

        return PlayResult(prediction, None)