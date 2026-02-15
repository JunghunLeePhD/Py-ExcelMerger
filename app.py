import gradio as gr
import pandas as pd
import tempfile
from lib.utils import combine_files


def load_columns(files):
    try:
        df_combined = combine_files(files)
        return gr.update(
            choices=df_combined.columns.tolist(),
            value=[],
            visible=True
        )

    except Exception as _:
        return gr.update(
            choices=[],
            value=[]
        )


def filter_dropdown(selected_cols):
    if selected_cols:
        return gr.update(
            choices=selected_cols,
            value=selected_cols[0],
            visible=True
        )
    return gr.update(
        choices=[],
        value=None
    )


def process_files(files, agg_cols,  group_col):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df_combined = combine_files(files)

    if not agg_cols:
        return (
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=False),
            gr.update(visible=True)
        )

    if len(agg_cols) == 1:
        df_result = df_combined[agg_cols]
        df_result.to_csv(temp_file.name, index=False)
        return (
            temp_file.name,
            df_result,
            gr.update(visible=False),
            gr.update(visible=True)
        )

    agg_cols_without_group_col = list(set(agg_cols) - set([group_col]))
    agg_cols_without_duplicate = agg_cols_without_group_col + [group_col]

    agg_dict = {
        k: "sum" if v in ['int32', 'float32', 'int64', 'float64'] else lambda x: x.mode()[
            0] if not x.mode().empty else None
        for k, v in df_combined[agg_cols_without_group_col].dtypes.to_dict().items()
    }

    try:
        df_result = df_combined[agg_cols_without_duplicate].groupby(
            [group_col]).agg(agg_dict).reset_index()

    except Exception as e:
        raise gr.Error(f"Aggregation Failed: {str(e)}")

    df_result.to_csv(temp_file.name, index=False)

    return (
        temp_file.name,
        df_result,
        gr.update(visible=False),
        gr.update(visible=True)
    )


def reset_app():
    return (
        None,
        gr.update(
            value=[],
            choices=[]
        ),
        gr.update(
            choices=[],
            value=None
        ),
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
            label="Select Data Columns to Aggregate (Pool)",
            interactive=True,
            visible=False
        )

        group_dropdown = gr.Dropdown(
            label="Select Grouping Column",
            interactive=True,
            visible=False
        )

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

    agg_checkbox.change(
        fn=filter_dropdown,
        inputs=agg_checkbox,
        outputs=group_dropdown
    )

    process_btn.click(
        fn=process_files,
        inputs=[
            file_input,
            agg_checkbox,
            group_dropdown
        ],
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
            agg_checkbox,
            group_dropdown,
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
