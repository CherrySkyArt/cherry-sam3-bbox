from typing_extensions import override
from comfy_api.latest import ComfyExtension, io
from .sam3_segment import CherrySAM3Segment


class CherrySAM3Extension(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [CherrySAM3Segment]

async def comfy_entrypoint() -> CherrySAM3Extension:
    return CherrySAM3Extension()
