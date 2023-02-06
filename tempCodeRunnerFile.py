query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpassword_entry.get(),userentry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, Please login with new password',parent=window)
                window.destroy()