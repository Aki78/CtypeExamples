use std::slice;

#[no_mangle]
pub extern "C" fn sum_arrays(result: *mut f64, a: *const f64, b: *const f64, n: usize) {
    let result_slice = unsafe { slice::from_raw_parts_mut(result, n) };
    let a_slice = unsafe { slice::from_raw_parts(a, n) };
    let b_slice = unsafe { slice::from_raw_parts(b, n) };

    for i in 0..n {
        result_slice[i] = a_slice[i] + b_slice[i];
    }
}

