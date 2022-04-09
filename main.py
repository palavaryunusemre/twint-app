import twint
import pandas as pd
import nest_asyncio
nest_asyncio.apply()

c=twint.Config()


c.Search="kanşekeri"

c.Since= '2017-01-01'
c.Until= '2021-04-06'

c.Store_csv = True
c.Output="heartAndAge20190524.csv"
twint.run.Search(c)
