import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

