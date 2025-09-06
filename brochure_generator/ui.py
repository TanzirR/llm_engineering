import gradio as gr
from brochure import create_brochure

force_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

def launch_gradio_ui():
    gr.Interface(
        fn=create_brochure,
        inputs=[
            gr.Textbox(label="Company Name"),
            gr.Textbox(label="Company URL"),
            gr.Dropdown(label="Output Language", choices=["English", "Bengali"])
        ],
        outputs=[gr.Markdown(label="Brochure")],
        flagging_mode="never",
        js=force_dark_mode,
        title="AI Brochure Generator",
    ).launch(share=False)
