from datetime import datetime


def fn_app_log(message: str, error_trace: str = None) -> bool:
    global FILE_LOG
    try:
        with open(FILE_LOG / "log.txt", 'a') as file:
            file.write(f'|{f"LOG:{datetime.now()}":-^150}|\n')
            file.write(f'|{f"MESSAGE: {message}": <150}|\n')
            if error_trace:
                file.write(error_trace)
                file.write('\n')
            file.write(f'|{f"END LOG":-^150}|\n')
    except Exception as e:
        return False
    else:
        return True
