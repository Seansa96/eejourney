Tags: [[netsec]]

This refers to the encryption of individual volumes on a system, which refers to a **formatted region of memory with an accompanying file system.** This is essentially a partition that has been given order. In this case, this also means that an encrypted volume encrypts things at the block/sector level, and that even unallocated or empty sectors are encrypted to prevent leakage, as well as metadata regarding structure.

This means that, if that data is exfiltrated to another device, it cannot be decrypted or otherwise accessed, as that actor lacks the keys necessary to do so.

These keys may be stored in an external module or a different partition/volume of that drive.  To provide integrity to the boot volume, which also must be readable in most consumer/business cases, a typical security measure is to keep a record of the hashes of various boot measurements, such as

* BIOS/UEFI Firmware
* Boot Manager
* Boot Configuration Data (BCD)
* OS Loader (winload.efi)

If the hashes mismatch, then that is proof that the data in this sector has been corrupted or altered in some fashion, and the TPM or other module will refuse to release the volume decryption key.