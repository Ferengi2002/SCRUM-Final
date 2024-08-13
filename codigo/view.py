class MathView:
    """Vista que maneja la interacción con el usuario."""

    @staticmethod
    def get_level():
        """Solicita al usuario que seleccione su nivel educativo."""
        return int(input("Selecciona tu nivel educativo (2: Segundo, 3: Tercero, 4: Cuarto): "))

    @staticmethod
    def get_total_questions():
        """Solicita al usuario la cantidad de preguntas."""
        return int(input("¿Cuántas preguntas te gustaría responder? "))

    @staticmethod
    def show_question(question):
        """Muestra una pregunta y captura la respuesta del usuario."""
        return int(input(f"¿Cuánto es {question}? "))

    @staticmethod
    def show_result(is_correct, correct_answer):
        """Muestra si la respuesta del usuario es correcta o no."""
        if is_correct:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es {correct_answer}.")

    @staticmethod
    def show_final_report(total_questions, correct_count, total_time):
        """Muestra un reporte final de los resultados."""
        print("\n*** Reporte Final ***")
        print(f"Preguntas totales: {total_questions}")
        print(f"Respuestas correctas: {correct_count}")
        print(f"Respuestas incorrectas: {total_questions - correct_count}")
        print(f"Porcentaje de aciertos: {correct_count / total_questions * 100:.2f}%")
        print(f"Tiempo total: {total_time:.2f} segundos")
        print(f"Promedio de tiempo por pregunta: {total_time / total_questions:.2f} segundos")
        print("¡Gracias por jugar!")

