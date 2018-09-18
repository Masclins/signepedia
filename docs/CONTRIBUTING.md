# Contributing

## Issues
An Issue should explain a specific problem.

Every Issue should begin with a verb describing the main action that should be taken to solve the explained problem.

The main comment of the Issue should have:
- A clear and specific description of a problem.
- A clear and specific description of the wanted behaviour.
- Steps needed to reproduce the problem, if it's a bug.
- Proposals to solve the Issue, clearly and specificaly explaining what's been considered.

Remember to assign the Issue you are working on to yourself. Please, try to work on a single Issue.

## Pull-requests
Any Pull-request should resolve an Issue. Use the [keywords](https://help.github.com/articles/closing-issues-using-keywords/) in the main comment of the Pull-request to close its appropiate Issue.

# Developement
For any change or contribution, this is what is expected of you:

1. Announce within an Issue that you want it assigned to you (or open said Issue yourself).
2. Do not take on more than one Issue at a time.
3. Design the tests for your Issue (unit tests will always be required).
4. Make them pass.
5. Repeat steps 3 and 4 until the Issue is solved.
5. Create a Pull-request and ask for a review from a collaborator
6. If changes are requested or travis does not pass, go to step 3.

## Running Unit tests

### Backend
`docker-compose run backend python3 test.py`

### Frontend
`docker-compose run frontend npm test`
