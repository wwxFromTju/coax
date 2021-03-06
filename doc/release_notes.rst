Release Notes
=============


v0.1.4
------

Implemented Prioritized Experience Replay:

- Implemented :class:`SegmentTree <coax.experience_replay.SegmentTree>` that allows for *batched*
  updating.
- Implemented :class:`SumTree <coax.experience_replay.SumTree>` subclass that allows for *batched*
  weighted sampling.
- Drop TransitionSingle (only use :class:`TransitionBatch <coax.reward_tracing.TransitionBatch>`
  from now on).
- Added :func:`TransitionBatch.from_single <coax.reward_tracing.TransitionBatch.from_single>`
  constructor.
- Added :attr:`TransitionBatch.idx <coax.reward_tracing.TransitionBatch.idx>` field to identify
  specific transitions.
- Added :attr:`TransitionBatch.W <coax.reward_tracing.TransitionBatch.W>` field to collect sample
  weights
- Made all :mod:`td_learning <coax.td_learning>` and :mod:`policy_objectives
  <coax.policy_objectives>` updaters compatible with :attr:`TransitionBatch.W
  <coax.reward_tracing.TransitionBatch.W>`
- Implemented the :class:`PrioritizedReplayBuffer <coax.experience_replay.PrioritizedReplayBuffer>`
  class itself.
- Added scripts and notebooks: :doc:`agent stub <examples/stubs/dqn_per>` and :doc:`pong
  <examples/atari/dqn_per>`.


Other utilities:

- Added :class:`FrameStacking <coax.wrappers.FrameStacking>` wrapper that respects the
  :mod:`gym.space` API and is compatible with the :mod:`jax.tree_util` module.
- Added data summary (min, median, max) for arrays in :class:`pretty_repr <coax.utils.pretty_repr>`
  util.
- Added :class:`StepwiseLinearFunction <coax.utils.StepwiseLinearFunction>` utility, which is handy
  for hyperparameter schedules, see example usage :doc:`here <examples/stubs/dqn_per>`.





v0.1.3
------

Implemented Distributional RL algorithm:

- Added two new methods to all proba_dists: :attr:`mean` and :attr:`affine_transform`, see
  :mod:`coax.proba_dists`.
- Made TD-learning updaters compatible with :class:`coax.StochasticV` and :class:`coax.StochasticQ`.
- Made value-based policies compatible with :class:`coax.StochasticQ`.


v0.1.2
------

First version to go public.
