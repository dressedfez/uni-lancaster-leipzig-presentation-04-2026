# /// script
# dependencies = [
#     "marimo",
#     "mcp==1.26.0",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.21.1"
app = marimo.App(
    width="full",
    layout_file="layouts/Dr_Frank_Zimmer_Inheritance_vs_Composition_in_Object_Oriented_Programming.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.Html("""
    <div style="display:flex; flex-direction:column; align-items:center;
                justify-content:center; height:80vh; text-align:center;">
      <h1 style="font-size:3rem;">Inhertiance vs. Composition in Object-Oriented Programming</h1>
      <h2 style="font-weight:normal; color:#555;">Dr. Frank Zimmer</h2>
      <p style="color:#888;">April 2026</p>
    </div>
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## Software-Development - From Problem to Software Design
    """),
            mo.center(
                mo.image("pictures/software-development-lifecycle.png", width=500)
            ),
            mo.md(r"""
    ## Design Questions

    - Is something a type of something else?  -- Entities have a **is-a** relationship
    - Does ist use something else to do its job? -- Entities have a **has-a** relationship

    /// note
    The way we answer these questions allows us to determine whether we deal with inheritance (**is-a**) or composition (**has-a**).
    ///
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""## Inheritance"""),
            mo.hstack(
                [
                    mo.vstack(
                        [
                            mo.center(
                                mo.image(
                                    "pictures/inheritance-with-counter-example.png",
                                    width="80%",
                                )
                            ),
                            mo.center(
                                mo.md("""
                        - a Car `is-a` Vehicle
                        - a Plane `is-a` Vehicle
                        - but a Plane `is-not-a` Car
                    """)
                            ),
                        ]
                    ),
                    mo.center(
                        mo.md("""
    /// attention
    - Inhertiance is described as an **is-a** relationship!
    - Sub-class inherites from or extends a base class, which means that:
      - behavior and
      - attributes of the base class are available in the sub-class.
    - This allows us to reuse code and create a hierarchical relationship between classes.
    ///""")
                    ),
                ]
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    example_code = """
    ###############################################
    # definition of base class and its behavior
    ###############################################
    class Vehicle: 

        def move(self):
              print("The vehicle moves")


    ###############################################
    # definition of sub-classes and their behavior
    ###############################################

    class Car(Vehicle):

        def honk(self):
            print("Car honks.")    # allows adding additional behavior without modifying the base class

    class Plane(Vehicle):

        def move(self):
            print("The plane flies.") # allows changing behavior without modifying the base class
            """
    mo.vstack(
        [
            mo.md("## Inheritance in Python"),
            mo.md(f"```python\n{example_code}\n```"),
        ]
    )
    return


@app.cell
def _():
    class Vehicle:
        def move(self):
            print(f"The vehicle ({type(self)}) moves")


    class Car(Vehicle):
        def honk(self):
            print("Car honks.")


    class Plane(Vehicle):
        def move(self):
            print("The plane flies.")

    return Car, Plane


@app.cell(hide_code=True)
def _(Car, Plane, mo):
    from contextlib import redirect_stdout
    import io

    snippet = """car = Car()
    car.move()
    car.honk()

    plane = Plane()
    plane.move()"""

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        car = Car()
        car.move()
        car.honk()

        plane = Plane()
        plane.move()

    mo.vstack(
        [
            mo.md("## Executed Example"),
            mo.md(f"```python\n{snippet}\n```"),
        ]
    )
    return buffer, io, redirect_stdout, snippet


@app.cell
def _(buffer, mo, snippet):
    mo.vstack(
        [
            mo.md("## Executed Example"),
            mo.md(f"```python\n{snippet}\n```"),
            mo.md(f"```text\n{buffer.getvalue().strip()}\n```"),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note
    - **Advantages of Inheritance:**
        - Inhertiance allows us to reuse code and create a hierarchical relationship between classes.
        - Extensibility: We can add new behavior to subclasses without modifying the base class.
    - **Disadvantages of Inheritance:**
        - Tight coupling: Subclasses are tightly coupled to the base class, which can lead to issues if the base class changes.
        - Inheritance can lead to complex hierarchies that are difficult to understand and maintain.
    ///
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""## Composition"""),
            mo.hstack(
                [
                    mo.center(mo.image("pictures/composition-example.png")),
                    mo.center(
                        mo.md(r"""
    /// attention
    - Composition is described as a **has-a** relationship!
    - In composition, a class contains an instance of another class to achieve its functionality, rather than inheriting from it.
    - Composite classes delegate behavior to their component classes
    ///
            """)
                    ),
                ],
                widths=[1.5, 1],
            ),
        ]
    )
    return


@app.cell
def _(mo):
    example_code_composition = """
    #########################################
    # definition of component class
    #########################################
    class Engine: 

        def start(self):
              print("Engine starts")


    ##########################################################
    # definition of composite or owner class and its behavior
    ##########################################################

    class CompositeCar:

        def __init__(self):
            print("Create a CompositeCar instance")
            self.engine = Engine()    # create an instance of Engine as a component of Car

        def start(self):
            print("CompositeCar starts")
            self.engine.start()      # delegate the start behavior to the Engine instance
    """
    mo.vstack(
        [
            mo.md("## Composition in Python"),
            mo.md(f"```python\n{example_code_composition}\n```"),
        ]
    )
    return


@app.cell
def _():
    class Engine:
        def start(self):
            print("Engine starts")


    class CompositeCar:
        def __init__(self):
            print("Create a CompositeCar instance")
            self.engine = (
                Engine()
            )  # create an instance of Engine as a component of Car

        def start(self):
            print("CompositeCar starts")
            self.engine.start()  # delegate the start behavior to the Engine instance

    return (CompositeCar,)


@app.cell
def _(CompositeCar, io, mo, redirect_stdout):
    snippet_composition = """
    composite_car = CompositeCar()

    composite_car.start()"""

    buffer_composition = io.StringIO()
    with redirect_stdout(buffer_composition):
        composite_car = CompositeCar()

        composite_car.start()

    mo.vstack(
        [
            mo.md("## Executed Example"),
            mo.md(f"```python\n{snippet_composition}\n```"),
        ]
    )
    return buffer_composition, snippet_composition


@app.cell
def _(buffer_composition, mo, snippet_composition):
    mo.vstack(
        [
            mo.md("## Executed Example"),
            mo.md(f"```python\n{snippet_composition}\n```"),
            mo.md(f"```text\n{buffer_composition.getvalue().strip()}\n```"),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    /// note
    - **Advantages of Composition:**
        - **Flexibility**: Composition allows us to change behavior (at runtime) by changing the component instances, e.g.
          ```python
          car.engine = ElectricEngine()
          ```
        - **Low Coupling**: changes in the component class do not affect the composite class as long as the interface remains consistent.
        - **Reusability**: Components can be reused across different composite classes, promoting code reuse and modularity.
        - **Avoids complex hierarchies**: Composition avoids the pitfalls of deep inheritance hierarchies.
    - **Disadvantages of Composition:**
        - **Boilerplate**: Composition can require more boilerplate code to delegate behavior to component classes.
        - **High Fragmentation**: Harder to understand the overall design as behavior is distributed across multiple classes.
        - **Indirection**: Behavior is spread across multiple classes.
    ///
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""## Comperision between Inheritance and Composition"""),
            mo.hstack(
                [
                    mo.md(r"""
    **Inheritance**:
    - **Relationship**: `is-a`
    - **Coupling**: Tight coupling between base and derived classes.
    - **Flexibility**: Less flexible, as behavior is defined in the class hierarchy.
    - **Code Reuse**: Promotes code reuse through class hierarchies.
    - **Use Case**: Suitable when there is a clear hierarchical relationship and shared behavior.
                """),
                    mo.md(r"""
    **Composition**:

    - **Relationship**: `has-a`
    - **Coupling**: Loose coupling between composite and component classes.
    - **Flexibility**: More flexible, as behavior can be changed at runtime by changing component instances.
    - **Code Reuse**: Promotes code reuse through composition of behaviors.
    - **Use Case**: Suitable when behavior can be achieved by combining simpler components, or when there is no clear hierarchical relationship.
                """),
                ]
            ),
            mo.md(r"""
            /// attention
            - Inheritance is simpler to start with, but composition scales better for complex systems. 
            - In practice, a combination of both is often used, with composition being favored for flexibility and maintainability.
            """),
        ],
        align="center",
    )
    return


@app.cell
def _(mo):
    mo.center(mo.image("pictures/thank-you-for-your-attention.png", width=500))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
