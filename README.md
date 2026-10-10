# Route Planner

Interactive obstacle grid with breadth-first shortest paths and a Dijkstra reference implementation.

An AI-assisted educational portfolio project prepared for Erik Vera's internship learning. This is a working prototype, not production software. Authorship and skills should be represented based on what you can explain and change independently.

## Try in your browser

[Open the live demo](https://erickvera610.github.io/route-planner/). The static JavaScript demo runs on the visitor's device and cannot change repository code. The Python implementation below provides the local backend. ML random-number generators differ between runtimes, so exact metrics differ. Tracker browser storage is localStorage; Python storage is SQLite.

## Run in two minutes

Requires Python 3.11 or newer; no pip dependencies.

```bash
git clone https://github.com/erickvera610/route-planner.git
cd route-planner
python app.py
```

Open http://127.0.0.1:8000. On Windows, use `py app.py` if `python` is unavailable. Stop with Ctrl+C. Run `python -m unittest discover -v` to execute tests.

## Architecture

- `index.html`: responsive accessible interface; renders output with textContent.
- `app.py`: local HTTP service, `/health`, and validated JSON POST `/api/run`.
- `core.py`: domain logic separated from transport and presentation.
- `test_core.py`: deterministic behavior and failure cases.
- `.github/workflows/tests.yml`: Python 3.11 and 3.12 CI.
- `TUTORIAL_ES.md`: beginner Spanish guide and interview practice.

## API

POST a JSON object to `/api/run`; inputs are the same fields used by the interface. Responses are JSON. Invalid inputs return 400; unknown paths return 404. GET `/health` returns `{"status":"ok"}`.

## Design and limits

Represento cada casilla como un nodo y cada movimiento como una arista. BFS explora por capas; como todos los movimientos cuestan uno, encuentra el camino más corto. parent permite reconstruir la ruta. La cola evita volver a explorar un nodo. Dijkstra usa una cola de prioridad y sirve para pesos no negativos; está incluido como referencia con pruebas. La interfaz utiliza BFS porque sus costos son iguales.

The built-in HTTP server is for a local demonstration. There is no authentication, rate limiting, or public production deployment. Never enter personal application records on a publicly exposed demo. Bind to localhost by default. For Codespaces only, run `HOST=0.0.0.0 python app.py` and keep the forwarded port private; usage may consume your GitHub quota.

## Review and contribution workflow

Create a feature branch, make one small change, run the tests, commit it, push the branch, and open a pull request. Explain the change and validation. Do not fabricate collaboration or commit history. Suggested first improvement: add a new input option with one behavior test and update this README.

## References

- https://docs.python.org/3/library/http.server.html
- https://docs.github.com/en/actions/tutorials/build-and-test-code/python

License: MIT.
