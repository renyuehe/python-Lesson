
//2、获取GIL实例
//线程在其他线程已经获取GIL的时候，需要通过pthread_cond_wait()等待获取GIL的线程释放GIL

/*获取GIL*/
int  PyThread_acquire_lock(PyThread_type_lock lock, int waitflag)
{
    int success;
    pthread_lock *thelock = (pthread_lock *)lock; /* 线程锁指针 */
    int status, error = 0;
    status = pthread_mutex_lock( &thelock->mut ); /* 上锁,先获取mutex, 获得操作locked变量的权限*/
    success = thelock->locked == 0;
    if ( !success && waitflag ) { /*表示已有线程上锁,*/
        while ( thelock->locked ) {
            /*通过pthread_cond_wait等待持有锁的线程释放锁*/
            status = pthread_cond_wait(&thelock->lock_released,
                                       &thelock->mut);
        }
        success = 1;
    }
    if (success) thelock->locked = 1; /*当前线程上锁*/
    status = pthread_mutex_unlock( &thelock->mut ); /*解锁mutex, 让其他线程有机会进入临界区等待上锁*/
    if (error) success = 0;
    return success;
}

//3、释放GIL实例
//特别注意最后一步, 通过pthread_cond_signal()通知其他等待(pthread_cond_wait())释放GIL的线程,让这些线程可以获取GIL。

/*释放GIL*/
void PyThread_release_lock(PyThread_type_lock lock)
{
    pthread_lock *thelock = (pthread_lock *)lock;
    int status, error = 0;
    status = pthread_mutex_lock( &thelock->mut ); /*上锁,通过mutex获取操作locked变量的权限*/
    thelock->locked = 0; /*实际的释放GIL的操作, 就是将locked置为0*/
    status = pthread_mutex_unlock( &thelock->mut ); /*解锁mutex*/
    status = pthread_cond_signal( &thelock->lock_released ); /*这步非常关键, 通知其他线程当前线程已经释放GIL*/
}