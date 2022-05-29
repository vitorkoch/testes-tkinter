import tkinter as tk
import requests


def feature_window():
    feature_window = tk.Tk()
    feature_window.title("Features")
    feature_window.resizable(0, 0)

    def advice():
        advice_toplevel = tk.Toplevel(feature_window)
        advice_toplevel.title("Advice")
        advice_toplevel.resizable(0, 0)

        def get_advice():
            random_advice = requests.get("https://api.adviceslip.com/advice")
            random_advice = random_advice.json()
            advice_label["text"] = random_advice["slip"]["advice"]

        advice_button = tk.Button(
            advice_toplevel, text="Advice", command=get_advice, width=15)
        advice_label = tk.Label(advice_toplevel, text="")
        advice_button.pack()
        advice_label.pack()
        advice_toplevel.mainloop()

    def pokedex():
        pokedex_toplevel = tk.Toplevel(feature_window)
        pokedex_toplevel.title("Pokedex")
        pokedex_toplevel.resizable(0, 0)

        poke_num_entry = tk.Entry(pokedex_toplevel)
        poke_num_entry.pack()

        def get_poke():
            poke_api = "https://pokeapi.co/api/v2/pokemon/{}"
            poke_num = int(poke_num_entry.get())
            get_poke = requests.get(poke_api.format(poke_num))
            get_poke = get_poke.json()
            poke_label["text"] = get_poke["name"].capitalize()

        poke_button = tk.Button(
            pokedex_toplevel, text="Pokedex", command=get_poke, width=15)
        poke_label = tk.Label(pokedex_toplevel, text="")
        poke_button.pack()
        poke_label.pack()
        pokedex_toplevel.mainloop()

    def chuck():
        chuck_toplevel = tk.Toplevel(feature_window)
        chuck_toplevel.title("Chuck")
        chuck_toplevel.resizable(0, 0)

        def get_chuck():
            random_chuck = requests.get(
                "https://api.chucknorris.io/jokes/random")
            random_chuck = random_chuck.json()
            chuck_label["text"] = random_chuck["value"]

        chuck_button = tk.Button(
            chuck_toplevel, text="Fun fact", command=get_chuck, width=15)
        chuck_label = tk.Label(chuck_toplevel, text="")
        chuck_button.pack()
        chuck_label.pack()
        chuck_toplevel.mainloop()

    def converter():
        converter_toplevel = tk.Toplevel(feature_window)
        converter_toplevel.title("Converter (OUT OF WORK)")
        converter_toplevel.resizable(0, 0)

        converter_toplevel.mainloop()

    # Buttons ----------------------
    advice_button = tk.Button(
        feature_window, text="Advice", command=advice, width=15)
    pokedex_button = tk.Button(
        feature_window, text="Pokedex", command=pokedex, width=15)
    chuck_button = tk.Button(
        feature_window, text="Chuck", command=chuck, width=15)
    converter_button = tk.Button(
        feature_window, text="Converter", command=converter, width=15)

    advice_button.grid(column=1, row=1)
    pokedex_button.grid(column=2, row=1)
    chuck_button.grid(column=1, row=2)
    converter_button.grid(column=2, row=2)

    feature_window.mainloop()


if __name__ == "__main__":
    feature_window()
