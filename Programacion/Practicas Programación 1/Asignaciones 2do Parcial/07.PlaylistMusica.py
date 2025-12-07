#GAJ278080
def gestionar_playlist():
    print("Desafío de Codificación: Tu Turno Playlist")
    
    playlist_musica = ["Bohemian Rhapsody", "Hotel California", "Stairway to Heaven"]
    print(f"\nLista inicial: {playlist_musica}")
    print("-" * 30)

    playlist_musica.append("Lejos de ti - Rels B")
    print("1. Agregada 'Lejos de ti' al final.")

    playlist_musica[1] = "Shape of You"
    print("2. 'Hotel California' cambiada por 'Shape of You'.")

    playlist_musica.insert(0, "Watermelon Sugar")
    print("3. 'Watermelon Sugar' insertada al inicio.")

    cancion_eliminada = playlist_musica.pop()
    print(f"4. Eliminada la última canción: '{cancion_eliminada}'.")

    print("-" * 30)
    
    total_canciones = len(playlist_musica)
    print(f"Lista Final: {playlist_musica}")
    print(f"Quedaron un total de {total_canciones} canciones.")


if __name__ == "__main__":
    gestionar_playlist()
