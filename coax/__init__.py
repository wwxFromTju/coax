# ------------------------------------------------------------------------------------------------ #
# MIT License                                                                                      #
#                                                                                                  #
# Copyright (c) 2020, Microsoft Corporation                                                        #
#                                                                                                  #
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software    #
# and associated documentation files (the "Software"), to deal in the Software without             #
# restriction, including without limitation the rights to use, copy, modify, merge, publish,       #
# distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the    #
# Software is furnished to do so, subject to the following conditions:                             #
#                                                                                                  #
# The above copyright notice and this permission notice shall be included in all copies or         #
# substantial portions of the Software.                                                            #
#                                                                                                  #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING    #
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND       #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,     #
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.          #
# ------------------------------------------------------------------------------------------------ #

__version__ = '0.1.0-rc1'


# expose specific classes and functions
from ._core.func_approx import FuncApprox
from ._core.value_v import V
from ._core.value_q import Q
from ._core.policy import Policy
from ._core.policy_q import EpsilonGreedy, BoltzmannPolicy
from ._core.policy_random import RandomPolicy
from ._core.experience_replay import ExperienceReplayBuffer
from ._core.episodic_cache import MonteCarloCache, NStepCache
from ._core.transition import TransitionBatch, TransitionSingle
from .utils import enable_logging

# pre-load submodules
from . import td_learning
from . import policy_objectives
from . import policy_regularizers
from . import proba_dists
from . import utils
from . import value_losses
from . import wrappers


__all__ = (

    # classes and functions
    'FuncApprox',
    'V',
    'Q',
    'Policy',
    'EpsilonGreedy',
    'BoltzmannPolicy',
    'RandomPolicy',
    'ExperienceReplayBuffer',
    'MonteCarloCache',
    'NStepCache',
    'TransitionBatch',
    'TransitionSingle',
    'enable_logging',

    # modules
    'td_learning',
    'policy_objectives',
    'policy_regularizers',
    'proba_dists',
    'utils',
    'value_losses',
    'wrappers',
)


# -----------------------------------------------------------------------------
# register envs
# -----------------------------------------------------------------------------

import gym

if 'ConnectFour-v0' in gym.envs.registry.env_specs:
    del gym.envs.registry.env_specs['ConnectFour-v0']

gym.envs.register(
    id='ConnectFour-v0',
    entry_point='coax.envs:ConnectFourEnv',
)


if 'FrozenLakeNonSlippery-v0' in gym.envs.registry.env_specs:
    del gym.envs.registry.env_specs['FrozenLakeNonSlippery-v0']

gym.envs.register(
    id='FrozenLakeNonSlippery-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False},
    max_episode_steps=20,
    reward_threshold=0.99,
)

del gym