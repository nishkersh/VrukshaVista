import openai

openai.api_key = "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"

assistant_id = "asst_XabNy3jaci7N3LdBF8xReIEE"

def add_message(thread_id, message):
    try:
        openai.beta.threads.messages.create(
            thread_id=thread_id, role="user", content=message
        )

    except Exception as e:
        pass

def run_thread(thread_id, assistant_id):
    try:
        run = openai.beta.threads.runs.create(
            thread_id=thread_id, assistant_id=assistant_id , instructions= "IF THIS MESSAGE IS NOT FOR YOU, JUST REPLY SOMTHING LIKE 'OH, LET'S WIAIT FOR HIM TO RESPOND'",
        )
        while run.status != "completed":
            run = openai.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)

    except Exception as e:
        pass

def get_last_message(thread_id):
    try:
        messages = openai.beta.threads.messages.list(thread_id=thread_id)
        return messages.data[0].content[0].text.value

    except Exception as e:
        pass
