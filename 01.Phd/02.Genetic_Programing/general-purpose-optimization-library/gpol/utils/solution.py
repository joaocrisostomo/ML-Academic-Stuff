import torch


class Solution:
    """ Implementation of a Solution class for any OP.

    The purpose of a Search Algorithm (SA) is to solve a given
    Optimization Problem (OP). The solve process consists of
    travelling across the solve space (𝑆) in a specific manner
    (which is embedded in algorithm's definition). This tour
    consists of generating solutions from 𝑆 and evaluating them
    trough 𝑓. In this context, a solution can be seen as the
    essential component in the mosaic composing this library.
    Concretely, it is the data structure which encapsulates the
    necessary attributes and behaviours in the context of the
    solve. More specifically, the unique identification, the
    representation under the light of a given OP, the validity
    state under the light of 𝑆, the fitness value(s) (which can
    be several, if training examples were partitioned).

    Notice that, to ease library's code-flexibility, the solutions'
    representation can take two forms: list or tensor. The former
    regards GP trees, the latter all the remaining representations
    (array-based).


    Attributes
    ----------
    _id : int
        A unique identification of a solution.
    valid : bool
        Solution's validity state under the light of 𝑆.
    repr_ : list
        The representation of a solution in 𝑆.
    fit: float
        A measure of quality in 𝑆. It is assigned by a given problem
        instance (PI), using fitness function (𝑓).
    """
    id_ = 0

    def __init__(self, repr_):
        """ Object's constructor.

        Parameters
        ----------
        repr_ : Object
            The representation of a solution in 𝑆.
        """
        self._id = Solution.id_
        Solution.id_ += 1
        self.repr_ = repr_
        self.valid = None
        self.fit = None

    def _get_copy(self):
        """ Makes a copy of the calling object.

        Notice that, to ease library's code-flexibility, the solutions'
        representation can take two forms: list or tensor. The former
        regards GP trees, the latter all the remaining representations
        (array-based).

        Returns
        -------
        solution : Solution
            An object of type Solution, copy of self.
        """
        if type(self.repr_) is torch.Tensor:
            sol_copy = Solution(self.repr_.clone())
        else:
            sol_copy = Solution(self.repr_.copy())
        if hasattr(self, 'valid'):
            sol_copy.valid = self.valid
        if hasattr(self, 'fit'):
            sol_copy.fit = self.fit.clone()
        if hasattr(self, 'test_fit'):
            sol_copy.val_fit = self.val_fit.clone()

        return sol_copy

    def __len__(self):
        return len(self.repr_)
