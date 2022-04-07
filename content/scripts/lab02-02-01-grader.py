# %% [markdown]
# # Lab 02.02.1: Marginals, Conditionals, and Joints

# %%
## Ignore this cell
!pip install ppdl==0.1.5 rlxmoocapi==0.1.0 --quiet

# %%
import inspect
from rlxmoocapi import submit, session
from ppdl.samplers import FluSeasonContactSampler

course_id = "ppdl.v1"
endpoint = "https://m5knaekxo6.execute-api.us-west-2.amazonaws.com/dev-v0001/rlxmooc"
lab = "L02.02.01"

# %% [markdown]
# Log-in with your username and password:

# %%
session.LoginSequence(
    endpoint=endpoint,
    course_id=course_id,
    lab_id=lab,
    varname="student"
    );

# %%
## TEACHER
import os
ses = session.Session(endpoint)
teacher = ses.login(
        user_id=os.environ["USER_ID"],
        pwd=os.environ["PASSWORD"],
        course_id=course_id,
        )

# %% [markdown]
# Base libraries:

# %%
import pandas as pd
import numpy as np

# %% [markdown]
# ## Task 1: Marginal Probabilities
#
# Consider the following probabilistic graphical model that represents the relationship between three random variables:
#
# <img src="img/1_graphical_model.svg" width="500px">
#
# * $\mathcal{X}_1 \in \{"Winter", "Spring", "Summer", "Autumn"\}$: the current season.
# * $\mathcal{X}_2 \in \{0, 1\}$: if a person had contact with another person with flu in the last week.
# * $\mathcal{Y} \in \{0, 1\}$: if a person has flu.
#
# Consider the following historical data:

# %%
sampler = FluSeasonContactSampler()
df = sampler(n_samples=1000, seed=42)
df

# %% [markdown]
# **CHALLENGE**: Implement a function that returns the marginal probability for a specific value in any of the three variables in the dataset:

# %%
def marginal(data, variable, value):
    """
    Implement this function to calculate the marginal probability of y.

    Parameters
    ----------
    data: DataFrame
        The dataframe containing the data.
    variable: str
        The variable to calculate the marginal probability of.
    value: str | int
        The value of the variable to calculate the marginal probability of.

    Returns
    -------
    prob : float
        The marginal probability of the variable in the given value.
    """
    ...

# %%
## TEACHER
def marginal(data, variable, value):
    return sum(data[variable] == value) / len(data)

# %% [markdown]
# Test your code, the following cases should be:
#
# ```python
# > marginal(df, "y", 1)
# 0.34
#
# > marginal(df, "x_1", "winter")
# 0.271
#
# > marginal(df, "x_2", 0)
# 0.482
# ```

# %%
marginal(df, "y", 1)

# %%
marginal(df, "x_1", "winter")

# %%
marginal(df, "x_2", 0)


# %%
## TEACHER

def grader1(functions, variables, caller_userid):
    from ppdl.samplers import FluSeasonContactSampler
    import numpy as np

    sampler = FluSeasonContactSampler()
    namespace = locals()
    for f in functions.values():
        exec(f, namespace)
    def marginal_sol(data, variable, value):
        return sum(data[variable] == value) / len(data)
    marginal_student = namespace["marginal"]
    msg = "Testing your code with 10 randomly generated datasets </br>"

    for _ in range(10):
        df = sampler(1000)
        combinations = {
                "x_1": ["winter", "spring", "summer", "autumn"],
                "x_2": [0, 1]
                }
        for variable, values in combinations.items():
            for value in values:
                sol_student = marginal_student(df, variable, value)
                sol_teacher = marginal_sol(df, variable, value)

                if not isinstance(sol_student, float):
                    msg += f"<b>Your code returned a non-float value for {variable} = {value}</b></br>"
                    return 0, msg
                elif not np.isclose(sol_student, sol_teacher):
                    msg += f"<b>Wrong answer!</b></br>"
                    return 0, msg
    return 5, msg + "<b>Success!</b>"

# %%
## TEACHER
source_functions = ["marginal"]
source_variables = []
teacher.run_grader_locally("grader1", source_functions, source_variables, locals())

# %%
## TEACHER
teacher.set_grader(
        teacher.course_id, lab, "T1",
        inspect.getsource(grader1), "grader1",
        source_functions, source_variables
        )

# %%
student.submit_task(namespace=globals(), task_id="T1");

# %% [markdown]
# ## Task 2: Conditional Probabilities
#
# Considering the same graphical model, consider the following historical data:

# %%
df = sampler(n_samples=1000, seed=0)
df

# %% [markdown]
# **CHALLENGE**: Implement the `conditional` function, so that it returns the conditional probability $P(\mathcal{Y}|\mathcal{X}_1, \mathcal{X}_2)$.

# %%
def conditional(data, x_1_value, x_2_value, y_value):
    """
    Implement this function to calculate the conditional probability of y.

    Parameters
    ----------
    data: DataFrame
        The dataframe containing the data.
    x_1_value: str
        Season
    x_2_value: int
        Contact
    y_value: int
        Flu

    Returns
    -------
    prob : float
        The conditional probability of the variable in the given value.
    """
    ...

# %%
## TEACHER
def conditional(data, x_1_value, x_2_value, y_value):
    condition = data.query("x_1 == @x_1_value and x_2 == @x_2_value")
    return sum(condition["y"] == y_value) / len(condition)

# %% [markdown]
# Test your code, the following cases should be:
#
# ```python
# > conditional(df, "spring", 0, 1)
# 0.1417
#
# > conditional(df, "winter", 1, 1)
# 0.6590
#
# > conditional(df, "autumn", 1, 0)
# 0.4919
# ```

# %%
# probability of flu given season is spring and contact is 0
conditional(df, "spring", 0, 1) 

# %%
# probability of flu given season is winter and contact is 1
conditional(df, "winter", 1, 1)

# %%
# probability of no flu given season is autumn and contact is 1
conditional(df, "autumn", 1, 0)

# %%
## TEACHER
def grader2(functions, variables, caller_userid):
    import numpy as np
    from ppdl.samplers import FluSeasonContactSampler

    sampler = FluSeasonContactSampler()
    namespace = locals()
    for f in functions.values():
        exec(f, namespace)
    def conditional_sol(data, x_1_value, x_2_value, y_value):
        condition = data.query("x_1 == @x_1_value and x_2 == @x_2_value")
        return sum(condition["y"] == y_value) / len(condition)
    
    conditional_student = namespace["conditional"]
    msg = "Testing your code with 3 randomly generated datasets </br>"

    for _ in range(3):
        df = sampler(1000)
        combinations = {
                "x_1": ["winter", "spring", "summer", "autumn"],
                "x_2": [0, 1],
                "y": [0, 1]
                }
        for _ in range(10):
            x_1 = np.random.choice(combinations["x_1"])
            x_2 = np.random.choice(combinations["x_2"])
            y = np.random.choice(combinations["y"])
            sol_student = conditional_student(df, x_1, x_2, y)
            sol_teacher = conditional_sol(df, x_1, x_2, y)

            if not isinstance(sol_student, float):
                msg += f"<b>Your code returned a non-float value </b></br>"
                return 0, msg
            elif not np.isclose(sol_student, sol_teacher):
                msg += f"<b>Wrong answer!</b></br>"
                return 0, msg
    return 5, msg + "<b>Success!</b>"

# %%
## TEACHER
source_functions = ["conditional"]
source_variables = []
teacher.run_grader_locally("grader2", source_functions, source_variables, locals())

# %%
## TEACHER
teacher.set_grader(
        teacher.course_id, lab, "T2",
        inspect.getsource(grader2), "grader2",
        source_functions, source_variables
        )

# %%
student.submit_task(namespace=globals(), task_id="T2");

# %% [markdown]
# ## Task 3: Joint Probabilities
#
# Consider the same graphical model, use the following historical data:

# %%
df = sampler(n_samples=1000, seed=20)
df

# %% [markdown]
# **CHALLENGE**: Implement the `joint` function, so that it returns the joint probability $P(\mathcal{Y}, \mathcal{X}_1, \mathcal{X}_2)$ for any input variable, you must use the functions from the task 1 and 2 by deducing an expression from the graphical model.

# %%
def joint(data, x_1_value, x_2_value, y_value):
    """
    Implement this function to calculate the joint probability.

    Parameters
    ----------
    data: DataFrame
        The dataframe containing the data.
    y_value: int
        If the person has flu.
    x_1_value: str | int
        The value of the first variable to calculate the joint probability of.
    x_2_value: str | int
        The value of the second variable to calculate the joint probability of.

    Returns
    -------
    prob : float
        The joint probability of the variable in the given value.
    """
    ...

# %%
## TEACHER
def joint(data, x_1_value, x_2_value, y_value):
    marginal_x1 = marginal(data, "x_1", x_1_value)
    marginal_x2 = marginal(data, "x_2", x_2_value)
    conditional_x1_x2 = conditional(data, x_1_value, x_2_value, y_value)
    return marginal_x1 * marginal_x2 * conditional_x1_x2

# %% [markdown]
# Test your code, the following cases should be:
#
# ```python
# > joint(df, "spring", 1, 0)
# 0.0923
#
# > joint(df, "winter", 1, 1)
# 0.0745
#
# > joint(df, "autumn", 1, 0)
# 0.0681
# ```

# %%
# probability of no flu and spring and contact 
joint(df, "spring", 1, 0)

# %%
# probability of flu and winter and contact
joint(df, "winter", 1, 1)

# %%
# probability of no flu and autumn and contact
joint(df, "autumn", 1, 0)

# %%
## TEACHER
def grader3(functions, variables, caller_userid):
    import numpy as np
    from ppdl.samplers import FluSeasonContactSampler

    namespace = locals()
    for f in functions.values():
        exec(f, namespace)
    
    marginal = namespace["marginal"]
    conditional = namespace["conditional"]
    joint_student = namespace["joint"]

    def marginal_sol(data, variable, value):
        return sum(data[variable] == value) / len(data)

    def conditional_sol(data, x_1_value, x_2_value, y_value):
        condition = data.query("x_1 == @x_1_value and x_2 == @x_2_value")
        return sum(condition["y"] == y_value) / len(condition)

    def joint_sol(data, x_1_value, x_2_value, y_value):
        marginal_x1 = marginal_sol(data, "x_1", x_1_value)
        marginal_x2 = marginal_sol(data, "x_2", x_2_value)
        conditional_x1_x2 = conditional_sol(data, x_1_value, x_2_value, y_value)
        return marginal_x1 * marginal_x2 * conditional_x1_x2

    msg = "Testing your code with 3 randomly generated datasets </br>"

    for _ in range(3):
        df = sampler(1000)
        combinations = {
                "x_1": ["winter", "spring", "summer", "autumn"],
                "x_2": [0, 1],
                "y": [0, 1]
                }
        for _ in range(10):
            x_1 = np.random.choice(combinations["x_1"])
            x_2 = np.random.choice(combinations["x_2"])
            y = np.random.choice(combinations["y"])
            sol_student = joint_student(df, x_1, x_2, y)
            sol_teacher = joint_sol(df, x_1, x_2, y)

            if not isinstance(sol_student, float):
                msg += f"<b>Your code returned a non-float value </b></br>"
                return 0, msg
            elif not np.isclose(sol_student, sol_teacher):
                msg += f"<b>Wrong answer!</b></br>"
                return 0, msg
    return 5, msg + "<b>Success!</b>"

# %%
## TEACHER
source_functions = ["joint", "marginal", "conditional"]
source_variables = []
teacher.run_grader_locally("grader3", source_functions, source_variables, locals())

# %%
## TEACHER
teacher.set_grader(
        teacher.course_id, lab, "T3",
        inspect.getsource(grader3), "grader3",
        source_functions, source_variables
        )

# %%
student.submit_task(namespace=globals(), task_id="T3");
