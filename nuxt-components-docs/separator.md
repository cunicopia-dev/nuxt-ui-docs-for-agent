<!-- source: https://ui.nuxt.com/components/separator --> # Separator

[Separator](https://reka-
ui.com/docs/components/separator)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Separator.vue)

Separates content horizontally or vertically.

## Usage

Use the Separator component as-is to separate content.

    
    
    <template>
      <USeparator />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the Separator.
Defaults to `horizontal`.

orientation

vertical

    
    
    <template>
      <USeparator orientation="vertical" class="h-48" />
    </template>
    

### Label

Use the `label` prop to display a label in the middle of the Separator.

label

    
    
    <template>
      <USeparator label="Hello World" />
    </template>
    

### Icon

Use the `icon` prop to display an icon in the middle of the Separator.

icon

    
    
    <template>
      <USeparator icon="i-simple-icons-nuxtdotjs" />
    </template>
    

### Avatar

Use the `avatar` prop to display an avatar in the middle of the Separator.

avatar.src

    
    
    <template>
      <USeparator
        :avatar="{
          src: 'https://github.com/nuxt.png'
        }"
      />
    </template>
    

### Color

Use the `color` prop to change the color of the Separator. Defaults to
`neutral`.

color

primary

type

solid

    
    
    <template>
      <USeparator color="primary" type="solid" />
    </template>
    

### Type

Use the `type` prop to change the type of the Separator. Defaults to `solid`.

type

dashed

    
    
    <template>
      <USeparator type="dashed" />
    </template>
    

### Size

Use the `size` prop to change the size of the Separator. Defaults to `xs`.

size

lg

    
    
    <template>
      <USeparator size="lg" />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`label`| | ` string`Display a label in the middle.  
`icon`| | ` string`Display an icon in the middle.  
`avatar`| | ` AvatarProps`Display an avatar in the middle.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "3xs" | "sm" | "2xs" | "md" | "xs" | "lg" | "xl" | "2xl" | "3xl"`Defaults to `'md'`.
  * `class?: any`
  * `style?: any`
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`

  
`color`| `'neutral'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`size`| `'xs'`| ` "sm" | "md" | "xs" | "lg" | "xl"`  
`type`| `'solid'`| ` "solid" | "dashed" | "dotted"`  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`The orientation of the separator.  
`decorative`| | `boolean`Whether or not the component is purely decorative.   
When `true`, accessibility-related attributes are updated so that that the
rendered element is removed from the accessibility tree.  
`ui`| | ` { root?: ClassNameValue; border?: ClassNameValue; container?: ClassNameValue; icon?: ClassNameValue; avatar?: ClassNameValue; avatarSize?: ClassNameValue; label?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        separator: {
          slots: {
            root: 'flex items-center align-center text-center',
            border: '',
            container: 'font-medium text-default flex',
            icon: 'shrink-0 size-5',
            avatar: 'shrink-0',
            avatarSize: '2xs',
            label: 'text-sm'
          },
          variants: {
            color: {
              primary: {
                border: 'border-primary'
              },
              secondary: {
                border: 'border-secondary'
              },
              success: {
                border: 'border-success'
              },
              info: {
                border: 'border-info'
              },
              warning: {
                border: 'border-warning'
              },
              error: {
                border: 'border-error'
              },
              neutral: {
                border: 'border-default'
              }
            },
            orientation: {
              horizontal: {
                root: 'w-full flex-row',
                border: 'w-full',
                container: 'mx-3 whitespace-nowrap'
              },
              vertical: {
                root: 'h-full flex-col',
                border: 'h-full',
                container: 'my-2'
              }
            },
            size: {
              xs: '',
              sm: '',
              md: '',
              lg: '',
              xl: ''
            },
            type: {
              solid: {
                border: 'border-solid'
              },
              dashed: {
                border: 'border-dashed'
              },
              dotted: {
                border: 'border-dotted'
              }
            }
          },
          compoundVariants: [
            {
              orientation: 'horizontal',
              size: 'xs',
              class: {
                border: 'border-t'
              }
            },
            {
              orientation: 'horizontal',
              size: 'sm',
              class: {
                border: 'border-t-[2px]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'md',
              class: {
                border: 'border-t-[3px]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'lg',
              class: {
                border: 'border-t-[4px]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'xl',
              class: {
                border: 'border-t-[5px]'
              }
            },
            {
              orientation: 'vertical',
              size: 'xs',
              class: {
                border: 'border-s'
              }
            },
            {
              orientation: 'vertical',
              size: 'sm',
              class: {
                border: 'border-s-[2px]'
              }
            },
            {
              orientation: 'vertical',
              size: 'md',
              class: {
                border: 'border-s-[3px]'
              }
            },
            {
              orientation: 'vertical',
              size: 'lg',
              class: {
                border: 'border-s-[4px]'
              }
            },
            {
              orientation: 'vertical',
              size: 'xl',
              class: {
                border: 'border-s-[5px]'
              }
            }
          ],
          defaultVariants: {
            color: 'neutral',
            size: 'xs',
            type: 'solid'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            separator: {
              slots: {
                root: 'flex items-center align-center text-center',
                border: '',
                container: 'font-medium text-default flex',
                icon: 'shrink-0 size-5',
                avatar: 'shrink-0',
                avatarSize: '2xs',
                label: 'text-sm'
              },
              variants: {
                color: {
                  primary: {
                    border: 'border-primary'
                  },
                  secondary: {
                    border: 'border-secondary'
                  },
                  success: {
                    border: 'border-success'
                  },
                  info: {
                    border: 'border-info'
                  },
                  warning: {
                    border: 'border-warning'
                  },
                  error: {
                    border: 'border-error'
                  },
                  neutral: {
                    border: 'border-default'
                  }
                },
                orientation: {
                  horizontal: {
                    root: 'w-full flex-row',
                    border: 'w-full',
                    container: 'mx-3 whitespace-nowrap'
                  },
                  vertical: {
                    root: 'h-full flex-col',
                    border: 'h-full',
                    container: 'my-2'
                  }
                },
                size: {
                  xs: '',
                  sm: '',
                  md: '',
                  lg: '',
                  xl: ''
                },
                type: {
                  solid: {
                    border: 'border-solid'
                  },
                  dashed: {
                    border: 'border-dashed'
                  },
                  dotted: {
                    border: 'border-dotted'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  size: 'xs',
                  class: {
                    border: 'border-t'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'sm',
                  class: {
                    border: 'border-t-[2px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'md',
                  class: {
                    border: 'border-t-[3px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'lg',
                  class: {
                    border: 'border-t-[4px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'xl',
                  class: {
                    border: 'border-t-[5px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xs',
                  class: {
                    border: 'border-s'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'sm',
                  class: {
                    border: 'border-s-[2px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'md',
                  class: {
                    border: 'border-s-[3px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'lg',
                  class: {
                    border: 'border-s-[4px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xl',
                  class: {
                    border: 'border-s-[5px]'
                  }
                }
              ],
              defaultVariants: {
                color: 'neutral',
                size: 'xs',
                type: 'solid'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            separator: {
              slots: {
                root: 'flex items-center align-center text-center',
                border: '',
                container: 'font-medium text-default flex',
                icon: 'shrink-0 size-5',
                avatar: 'shrink-0',
                avatarSize: '2xs',
                label: 'text-sm'
              },
              variants: {
                color: {
                  primary: {
                    border: 'border-primary'
                  },
                  secondary: {
                    border: 'border-secondary'
                  },
                  success: {
                    border: 'border-success'
                  },
                  info: {
                    border: 'border-info'
                  },
                  warning: {
                    border: 'border-warning'
                  },
                  error: {
                    border: 'border-error'
                  },
                  neutral: {
                    border: 'border-default'
                  }
                },
                orientation: {
                  horizontal: {
                    root: 'w-full flex-row',
                    border: 'w-full',
                    container: 'mx-3 whitespace-nowrap'
                  },
                  vertical: {
                    root: 'h-full flex-col',
                    border: 'h-full',
                    container: 'my-2'
                  }
                },
                size: {
                  xs: '',
                  sm: '',
                  md: '',
                  lg: '',
                  xl: ''
                },
                type: {
                  solid: {
                    border: 'border-solid'
                  },
                  dashed: {
                    border: 'border-dashed'
                  },
                  dotted: {
                    border: 'border-dotted'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  size: 'xs',
                  class: {
                    border: 'border-t'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'sm',
                  class: {
                    border: 'border-t-[2px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'md',
                  class: {
                    border: 'border-t-[3px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'lg',
                  class: {
                    border: 'border-t-[4px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'xl',
                  class: {
                    border: 'border-t-[5px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xs',
                  class: {
                    border: 'border-s'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'sm',
                  class: {
                    border: 'border-s-[2px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'md',
                  class: {
                    border: 'border-s-[3px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'lg',
                  class: {
                    border: 'border-s-[4px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xl',
                  class: {
                    border: 'border-s-[5px]'
                  }
                }
              ],
              defaultVariants: {
                color: 'neutral',
                size: 'xs',
                type: 'solid'
              }
            }
          }
        })
      ]
    })
    

Expand code

[SelectMenuAn advanced searchable select element.](/components/select-
menu)[SkeletonA placeholder to show while content is
loading.](/components/skeleton)

