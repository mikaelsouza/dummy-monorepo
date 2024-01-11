python_requirements(
    name="global-reqs",
    source="requirements/global.txt",
    resolve=parametrize(
        "monorepo", 
        "titanic",
    ),
)

python_requirements(
    name="titanic-reqs",
    source="requirements/titanic.txt",
    resolve="titanic",
)
