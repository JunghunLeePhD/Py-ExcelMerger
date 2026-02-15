import gradio as gr
import pandas as pd
import tempfile


def combine_files(files):
    try:
        dfs = [pd.read_excel(file.name) for file in files]
        return pd.concat(dfs, ignore_index=True)
    except Exception as _:
        return pd.DataFrame()


def load_columns(files):
    try:
        df_combined = combine_files(files)
        return gr.update(
            choices=df_combined.columns.tolist(),
            value=[]
        )

    except Exception as _:
        return gr.update(
            choices=[],
            value=[]
        )


def process_files(files):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df_combined = combine_files(files)
    return (
        temp_file.name,
        df_combined,
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

        agg_checkbox = gr.CheckboxGroup(
            label="Select Data Columns to Aggregate (Pool)", interactive=True)

        process_btn = gr.Button(
            "Process Files 🚀",
            variant="primary"
        )

    with gr.Column(visible=False) as result_view:
        gr.Markdown("### Step 2/2: Preview and Download Results")
        reset_btn = gr.Button("🔄 Start Over")
        download_btn = gr.File(label="Download CSV")
        output_df = gr.DataFrame(label="Preview Result", interactive=False)

    file_input.upload(
        fn=load_columns,
        inputs=file_input,
        outputs=[agg_checkbox]
    )

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
