Title: Decklink SDI Linux 2.6.36
Date: 2010-10-19 12:42
Category: Informatique // IT
Tags: GNU/Linux, Blackmagic Design, Decklink
Slug: decklink-sdi-linux-2-6-36
Status: published

Here's a patch allowing the
[blackmagic](http://www.blackmagic-design.com/) kernel module to  
  
build against 2.6.36 linux kernel.

    Signed-off-by: Raphaël Doursenaud 
    ---
    diff -Nurp DeckLink-7.9rc7/blackmagic_core.c DeckLink-7.9rc7-2.6.36/blackmagic_core.c
    --- DeckLink-7.9rc7/blackmagic_core.c   2010-10-19 12:08:30.153000030 +0200
    +++ DeckLink-7.9rc7-2.6.36/blackmagic_core.c    2010-10-19 12:25:51.448000032 +0200
    @@ -164,7 +164,12 @@ static irqreturn_t blackmagic_isr(int ir
     static int blackmagic_open(struct inode *inode, struct file *filp)
     {
        struct blackmagic_device *ddev;
    +#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 36)
    +   ddev = filp->private_data;
    +#else
        ddev = blackmagic_find_device_by_minor(iminor(inode));
    +#endif
    +
        if (!ddev)
            return -ENODEV;
        
    @@ -181,7 +186,12 @@ static int blackmagic_open(struct inode
     static int blackmagic_release(struct inode *inode, struct file *filp)
     {
        struct blackmagic_device *ddev;
    +#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 36)
    +   ddev = filp->private_data;
    +#else
        ddev = blackmagic_find_device_by_minor(iminor(inode));
    +#endif
    +
        if (!ddev)
            return -ENODEV;
     
    @@ -196,20 +206,33 @@ static int blackmagic_release(struct ino
        return 0;
     }
     
    +#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 36)
    +static long
    +blackmagic_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)
    +#else
     static int
     blackmagic_ioctl(struct inode *inode, struct file *filp,
                    unsigned int cmd, unsigned long arg)
    +#endif
     {
        struct blackmagic_device *ddev;
    +#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 36)
    +   ddev = filp->private_data;
    +#else
        ddev = blackmagic_find_device_by_minor(iminor(inode));
    +#endif
        
        if (!ddev)
            return -ENODEV;
        
        if (!filp->private_data)
            return -ENODEV;
    -   
    +
    +#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 36)
    +   return blackmagic_ioctl_private(filp->private_data, cmd, arg);
    +#else
        return blackmagic_ioctl_private(ddev->driver, filp->private_data, cmd, arg);
    +#endif
     }
     
     /*
    @@ -226,7 +249,11 @@ struct file_operations blackmagic_fops =
        .owner   = THIS_MODULE,
        .open = blackmagic_open,
        .release = blackmagic_release,
    +#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 36)
    +   .unlocked_ioctl = blackmagic_ioctl,
    +#else
        .ioctl = blackmagic_ioctl,
    +#endif
        .poll = blackmagic_poll,
     };
     
    diff -Nurp DeckLink-7.9rc7/blackmagic_iml.h DeckLink-7.9rc7-2.6.36/blackmagic_iml.h
    --- DeckLink-7.9rc7/blackmagic_iml.h    2010-10-19 12:08:30.154000030 +0200
    +++ DeckLink-7.9rc7-2.6.36/blackmagic_iml.h 2010-10-19 12:07:15.949000030 +0200
    @@ -35,7 +35,11 @@ extern "C" {
     #endif
     
     /* Init and Startup */
    +#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 36)
    +extern int blackmagic_ioctl_private(void *, unsigned int, unsigned long);
    +#else
     extern int blackmagic_ioctl_private(void *, void *, unsigned int, unsigned long);
    +#endif
     extern void *dl_create_and_start_driver(void *, unsigned int *);
     extern void *dl_create_and_init_user_client(void *, void *);
     extern void dl_release_user_client(void *);
    diff -Nurp DeckLink-7.9rc7/blackmagic_lib.c DeckLink-7.9rc7-2.6.36/blackmagic_lib.c
    --- DeckLink-7.9rc7/blackmagic_lib.c    2010-10-19 12:08:30.154000030 +0200
    +++ DeckLink-7.9rc7-2.6.36/blackmagic_lib.c 2010-10-19 12:07:15.949000030 +0200
    @@ -725,7 +725,9 @@ dl_kernel_fpu_begin()
            #define FX_SAVE_INSTR   "fxsave %0; fnclex"
     #endif
     
    -#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 26)
    +#if LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 35)
    +       asm volatile(FX_SAVE_INSTR : "=m" (thread->task->thread.fpu.state->fxsave));
    +#elif LINUX_VERSION_CODE >= KERNEL_VERSION(2, 6, 26)
            asm volatile(FX_SAVE_INSTR : "=m" (thread->task->thread.xstate->fxsave));
     #else
            asm volatile(FX_SAVE_INSTR : "=m" (thread->task->thread.i387.fxsave));
