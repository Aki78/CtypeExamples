{-# LANGUAGE ForeignFunctionInterface #-}

import Foreign.C.Types
import Foreign.Marshal.Array
import Foreign.Ptr

foreign export ccall sum_arrays :: Ptr CDouble -> Ptr CDouble -> Ptr CDouble -> CInt -> IO ()

sum_arrays :: Ptr CDouble -> Ptr CDouble -> Ptr CDouble -> CInt -> IO ()
sum_arrays result a b n =
  let n' = fromIntegral n
  in  withArray (zipWith (+) (peekArray n' a) (peekArray n' b)) $ \sum ->
        pokeArray result sum
