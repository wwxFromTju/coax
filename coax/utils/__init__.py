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

r"""

Utilities
=========

This is a collection of utility (helper) functions used throughout the package.


Object Reference
----------------

.. autosummary::
    :nosignatures:

    coax.utils.OrnsteinUhlenbeckNoise
    coax.utils.StepwiseLinearFunction
    coax.utils.argmax
    coax.utils.argmin
    coax.utils.batch_to_single
    coax.utils.check_array
    coax.utils.check_preprocessors
    coax.utils.clipped_logit
    coax.utils.default_preprocessor
    coax.utils.diff_transform
    coax.utils.diff_transform_matrix
    coax.utils.docstring
    coax.utils.double_relu
    coax.utils.enable_logging
    coax.utils.generate_gif
    coax.utils.get_env_attr
    coax.utils.get_grads_diagnostics
    coax.utils.get_magnitude_quantiles
    coax.utils.get_transition_batch
    coax.utils.has_env_attr
    coax.utils.idx
    coax.utils.is_policy
    coax.utils.is_qfunction
    coax.utils.is_reward_function
    coax.utils.is_stochastic
    coax.utils.is_transition_model
    coax.utils.is_vfunction
    coax.utils.isscalar
    coax.utils.merge_dicts
    coax.utils.pretty_repr
    coax.utils.reload_recursive
    coax.utils.render_episode
    coax.utils.safe_sample
    coax.utils.single_to_batch
    coax.utils.tree_ravel


"""

from ._action_noise import (
    OrnsteinUhlenbeckNoise,
)
from ._array import (
    StepwiseLinearFunction,
    argmax,
    argmin,
    batch_to_single,
    check_array,
    check_preprocessors,
    clipped_logit,
    default_preprocessor,
    diff_transform,
    diff_transform_matrix,
    double_relu,
    get_grads_diagnostics,
    get_magnitude_quantiles,
    get_transition_batch,
    idx,
    isscalar,
    merge_dicts,
    safe_sample,
    single_to_batch,
    tree_ravel,
)
from ._misc import (
    docstring,
    enable_logging,
    generate_gif,
    get_env_attr,
    has_env_attr,
    is_policy,
    is_qfunction,
    is_reward_function,
    is_stochastic,
    is_transition_model,
    is_vfunction,
    pretty_repr,
    reload_recursive,
    render_episode,
)


__all__ = (
    'StepwiseLinearFunction',
    'OrnsteinUhlenbeckNoise',
    'argmax',
    'argmin',
    'batch_to_single',
    'check_array',
    'check_preprocessors',
    'clipped_logit',
    'default_preprocessor',
    'diff_transform',
    'diff_transform_matrix',
    'docstring',
    'double_relu',
    'enable_logging',
    'generate_gif',
    'get_env_attr',
    'get_grads_diagnostics',
    'get_magnitude_quantiles',
    'get_transition_batch',
    'has_env_attr',
    'idx',
    'is_policy',
    'is_qfunction',
    'is_reward_function',
    'is_stochastic',
    'is_transition_model',
    'is_vfunction',
    'isscalar',
    'merge_dicts',
    'pretty_repr',
    'reload_recursive',
    'render_episode',
    'safe_sample',
    'single_to_batch',
    'tree_ravel',
)
