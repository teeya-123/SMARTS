# MIT License
#
# Copyright (C) 2021. Huawei Technologies Co., Ltd. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import unittest, ray, os, sys
from ultra.rllib_train import train
import shutil

AGENT_ID = "001"
seed = 2


class RLlibTrainTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        if os.path.exists("tests/rllib_results"):
            shutil.rmtree("tests/rllib_results")

    def test_rllib_train_cli(self):
        ray.shutdown()
        log_dir = "tests/rllib_results"
        try:
            os.system(
                f"python ultra/rllib_train.py --task 00 --level easy --episodes 1 --max-samples 200 --headless True --log-dir {log_dir}"
            )
        except Exception as err:
            print(err)
            self.assertTrue(False)

        if os.path.exists(log_dir):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_rllib_train_method(self):
        log_dir = "tests/rllib_results"
        try:
            ray.shutdown()
            ray.init()
            train(
                task=("00", "easy"),
                num_episodes=1,
                eval_info={
                    "eval_rate": 2,
                    "eval_episodes": 1,
                },
                timestep_sec=0.1,
                headless=True,
                seed=2,
                max_samples=200,
                log_dir=log_dir,
            )
        except Exception as err:
            print(err)
            self.assertTrue(False)

        if os.path.exists(log_dir):
            self.assertTrue(True)
        else:
            self.assertTrue(False)
