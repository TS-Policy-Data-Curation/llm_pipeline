import sycamore
from sycamore.context import ExecMode
from sycamore.materialize import AutoMaterialize
from sycamore.utils.pdf_utils import show_pages
from sycamore.data import Element
from sycamore.transforms.partition import ArynPartitioner
# DATA
#uris = ["s3://aryn-public/ntsb/0.pdf", "s3://aryn-public/ntsb/1.pdf", "s3://aryn-public/ntsb/10.pdf", "s3://aryn-public/ntsb/101.pdf", "s3://aryn-public/ntsb/103.pdf", "s3://aryn-public/ntsb/104.pdf", "s3://aryn-public/ntsb/11.pdf", "s3://aryn-public/ntsb/12.pdf", "s3://aryn-public/ntsb/16.pdf", "s3://aryn-public/ntsb/18.pdf", "s3://aryn-public/ntsb/20.pdf", "s3://aryn-public/ntsb/21.pdf", "s3://aryn-public/ntsb/22.pdf", "s3://aryn-public/ntsb/23.pdf"
#, "s3://aryn-public/ntsb/25.pdf", "s3://aryn-public/ntsb/26.pdf", "s3://aryn-public/ntsb/27.pdf", "s3://aryn-public/ntsb/28.pdf", "s3://aryn-public/ntsb/3.pdf", "s3://aryn-public/ntsb/31.pdf", "s3://aryn-public/ntsb/32.pdf", "s3://aryn-public/ntsb/34.pdf", "s3://aryn-public/ntsb/35.pdf", "s3://aryn-public/ntsb/36.pdf", "s3://aryn-public/ntsb/37.pdf", "s3://aryn-public/ntsb/38.pdf", "s3://aryn-public/ntsb/39.pdf"
#, "s3://aryn-public/ntsb/40.pdf", "s3://aryn-public/ntsb/41.pdf", "s3://aryn-public/ntsb/42.pdf"]
def load_docs(uris="s3://aryn-public/ntsb/"):
    ctx = sycamore.init(exec_mode=sycamore.EXEC_LOCAL)
    ctx.rewrite_rules.append(AutoMaterialize(source_mode=sycamore.MATERIALIZE_USE_STORED))
    docs = ctx.read.binary(paths=uris, binary_format="pdf")
    return docs