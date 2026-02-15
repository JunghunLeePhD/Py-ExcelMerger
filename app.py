import gradio as gr
import pandas as pd
import tempfile


def process_files(files):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    return (
        temp_file.name,
        files,
        gr.update(visible=False),
        gr.update(visible=True)
    )


def reset_app():
    return (
        None,
        None,
        None,
        gr.update(visible=True),
        gr.update(visible=False)
    )


with gr.Blocks(title="Excel Manipulator") as demo:
    gr.Markdown("# 📊 Excel Manipulator")

    with gr.Column(visible=True) as input_view:
        gr.Markdown("### Step 1/2: Upload & Configure")
        file_input = gr.File(
            label="Upload Excel Files",
            file_count="multiple",
            file_types=[".xlsx", ".xls"]
        )

        process_btn = gr.Button(
            "Process Files 🚀",
            variant="primary"
        )

    with gr.Column(visible=False) as result_view:
        gr.Markdown("### Step 2/2: Preview and Download Results")
        with gr.Row():
            download_btn = gr.File(label="Download CSV")
            reset_btn = gr.Button("🔄 Start Over")
        output_df = gr.DataFrame(label="Preview Result", interactive=False)

    process_btn.click(
        fn=process_files,
        inputs=[file_input],
        outputs=[
            download_btn,
            output_df,
            input_view,
            result_view
        ]
    )

    reset_btn.click(
        fn=reset_app,
        inputs=[],
        outputs=[
            file_input,
            download_btn,
            output_df,
            input_view,
            result_view
        ]
    )


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
